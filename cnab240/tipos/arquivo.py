# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals
import codecs
from datetime import datetime

from evento import Evento
from lote import Lote
from .. import errors
from ..constantes import (
    TIPO_REGISTRO_HEADER_ARQUIVO,
    TIPO_REGISTRO_HEADER_LOTE,
    TIPO_REGISTRO_DETALHE,
    TIPO_REGISTRO_TRAILER_LOTE,
    TIPO_REGISTRO_TRAILER_ARQUIVO,
    TIPO_OPERACAO_ARQUIVO_RETORNO,
    TIPO_SERVICO_COBRANCA,
)


class Arquivo(object):

    def __init__(self, banco, **kwargs):
        """Arquivo Cnab240."""

        self._lotes = []
        self.banco = banco
        arquivo = kwargs.get('arquivo')
        if isinstance(arquivo, (file, codecs.StreamReaderWriter)):
            return self.carregar_retorno(arquivo)

        self.header = self.banco.registros.HeaderArquivo(**kwargs)
        self.trailer = self.banco.registros.TrailerArquivo(**kwargs)
        self.trailer.totais_quantidade_lotes = 0
        self.trailer.totais_quantidade_registros = 2

        if self.header.arquivo_data_de_geracao is None:
            now = datetime.now()
            self.header.arquivo_data_de_geracao = int(now.strftime("%d%m%Y"))

        # necessario pois o santander nao tem hora de geracao
        try:
            if self.header.arquivo_hora_de_geracao is None:
                if now is None:
                    now = datetime.now()
                self.header.arquivo_hora_de_geracao = int(
                    now.strftime("%H%M%S"))
        except AttributeError:
            pass

    def carregar_retorno(self, arquivo):

        lote_aberto = None
        evento_aberto = None

        for linha in arquivo:
            tipo_registro = linha[7]

            if tipo_registro == TIPO_REGISTRO_HEADER_ARQUIVO:

                self.header = self.banco.registros.HeaderArquivo()
                self.header.carregar(linha)

            elif tipo_registro == TIPO_REGISTRO_HEADER_LOTE:
                codigo_servico = linha[9:11]

                if codigo_servico == TIPO_SERVICO_COBRANCA:
                    header_lote = self.banco.registros.HeaderLoteCobranca()
                    header_lote.carregar(linha)
                    trailer_lote = self.banco.registros.TrailerLoteCobranca()
                    lote_aberto = Lote(self.banco, header_lote, trailer_lote)
                    self._lotes.append(lote_aberto)

            elif tipo_registro == TIPO_REGISTRO_DETALHE:
                tipo_segmento = linha[13]
                codigo_evento = linha[15:17]

                if tipo_segmento == TIPO_OPERACAO_ARQUIVO_RETORNO:
                    seg_t = self.banco.registros.SegmentoT()
                    seg_t.carregar(linha)

                    evento_aberto = Evento(self.banco, int(codigo_evento))
                    lote_aberto._eventos.append(evento_aberto)
                    evento_aberto._segmentos.append(seg_t)

                elif tipo_segmento == 'U':
                    seg_u = self.banco.registros.SegmentoU()
                    seg_u.carregar(linha)
                    evento_aberto._segmentos.append(seg_u)
                    evento_aberto = None

            elif tipo_registro == TIPO_REGISTRO_TRAILER_LOTE:
                if trailer_lote is not None:
                    lote_aberto.trailer.carregar(linha)
                else:
                    raise Exception

            elif tipo_registro == TIPO_REGISTRO_TRAILER_ARQUIVO:
                self.trailer = self.banco.registros.TrailerArquivo()
                self.trailer.carregar(linha)

    @property
    def lotes(self):
        return self._lotes

    def incluir_cobranca(self, **kwargs):
        # 1 eh o codigo de cobranca
        codigo_evento = 1
        evento = Evento(self.banco, codigo_evento)

        seg_p = self.banco.registros.SegmentoP(**kwargs)
        evento.adicionar_segmento(seg_p)

        seg_q = self.banco.registros.SegmentoQ(**kwargs)
        evento.adicionar_segmento(seg_q)

        seg_r = self.banco.registros.SegmentoR(**kwargs)
        if seg_r.necessario():
            evento.adicionar_segmento(seg_r)

        lote_cobranca = self.encontrar_lote(codigo_evento)

        if lote_cobranca is None:
            header = self.banco.registros.HeaderLoteCobranca(
                **self.header.todict()
            )
            trailer = self.banco.registros.TrailerLoteCobranca()
            lote_cobranca = Lote(self.banco, header, trailer)

            self.adicionar_lote(lote_cobranca)

            if header.controlecob_numero is None:
                header.controlecob_numero = int('{0}{1:02}'.format(
                    self.header.arquivo_sequencia,
                    lote_cobranca.codigo))

            if header.controlecob_data_gravacao is None:
                header.controlecob_data_gravacao = \
                    self.header.arquivo_data_de_geracao

        lote_cobranca.adicionar_evento(evento)
        # Incrementar numero de registros no trailer do arquivo
        self.trailer.totais_quantidade_registros += len(evento)

    def incluir_debito_pagamento(self, seg_a=False, seg_b=False, **kwargs):
        # 1 eh o codigo de cobranca
        codigo_evento = 1
        evento = Evento(self.banco, codigo_evento)

        if not seg_a:
            seg_a = self.banco.registros.SegmentoA(**kwargs)
        evento.adicionar_segmento(seg_a)

        if not seg_b:
            seg_b = self.banco.registros.SegmentoB(**kwargs)
        evento.adicionar_segmento(seg_b)

        # seg_c = self.banco.registros.SegmentoC(**kwargs)
        # if seg_c.necessario():
        #     evento.adicionar_segmento(seg_c)

        lote_pagamento = self.encontrar_lote(codigo_evento)

        if lote_pagamento is None:
            header = self.banco.registros.HeaderLotePagamento(
                **self.header.todict()
            )
            trailer = self.banco.registros.TrailerLotePagamento()
            trailer.somatoria_valores = kwargs.get('credito_valor_pagamento')
            trailer.somatoria_quantidade_moedas = kwargs.get(
                'credito_moeda_quantidade')
            lote_pagamento = Lote(self.banco, header, trailer)

            self.adicionar_lote(lote_pagamento)
        else:
            lote_pagamento.trailer.somatoria_valores += \
                kwargs.get('credito_valor_pagamento')
            lote_pagamento.trailer.somatoria_quantidade_moedas += kwargs.get(
                'credito_moeda_quantidade')

        lote_pagamento.adicionar_evento(evento)
        # Incrementar numero de registros no trailer do arquivo
        self.trailer.totais_quantidade_registros += len(evento)

    def encontrar_lote(self, codigo_servico):
        for lote in self.lotes:
            if lote.header.servico_servico == codigo_servico:
                return lote

    def adicionar_lote(self, lote):
        if not isinstance(lote, Lote):
            raise TypeError('Objeto deve ser instancia de "Lote"')

        self._lotes.append(lote)
        lote.codigo = len(self._lotes)

        # Incrementar numero de lotes no trailer do arquivo
        self.trailer.totais_quantidade_lotes += 1

        # Incrementar numero de registros no trailer do arquivo
        self.trailer.totais_quantidade_registros += len(lote)

    def escrever(self, file_):
        file_.write(unicode(self).encode('ascii'))

    def __unicode__(self):
        if not self._lotes:
            raise errors.ArquivoVazioError()

        result = []
        result.append(unicode(self.header))
        result.extend(unicode(lote) for lote in self._lotes)
        result.append(unicode(self.trailer))
        # Adicionar elemento vazio para arquivo terminar com \r\n
        result.append(u'')
        return u'\r\n'.join(result)
