# -*- encoding: utf-8 -*-

import os

from datetime import datetime

class GeraCNAB240():

    def __init__(self, path, agencia, conta):
        self.path = path
        self.nome_arquivo = ''
        self.codigo_banco = 1
        self.lote_servico = 0
        self.tipo_registro = 0
        self.tipo_inscricao = None
        self.numero_inscricao = None
        self.agencia = agencia
        self.agencia_dv = 'X'
        self.numero_conta = conta
        self.conta_dv = 'X'
        self.dv = ''
        self.nome_empresa = None
        self.nome_banco = 'BANCO DO BRASIL - S.A.'
        self.codigo_remessa_retorno = 1
        self.data_geracao = None
        self.hora_geracao = None
        self.numero_sequencial = 0
        self.layout = 83
        self.densidade = 0
        self.lote = 1
        self.tipo_reg = 1
        self.tipo_operador = 'R'
        self.tipo_servico = 1
        self.layout_lote = 40
        self.numero_convenio = None
        self.cobranca_cedente = None
        self.numero_carteira = None
        self.variacao_carteira = None
        self.mensagem1 = ''
        self.mensagem2 = ''
        self.numero_remessa_retorno = None
        self.data_gravacao = None
        self.data_cretido = 0

        self.tipo_regP = 3
        self.sequencial_lote = 1
        self.segmentoP = 'P'
        self.cod_movimento_remessa = None
        self.identificacao_titulo = None
        self.codigo_carteira = None
        self.forma_cadastro = None
        self.tipo_doc = None
        self.ident_emissor_boleto = None
        self.ident_distribuicao = None
        self.numero_doc_cobranca = None
        self.data_vencimento = None
        self.valor = None
        self.agencia_cobranca = 0
        self.agencia_cobranca_dv = ''
        self.especie = None
        self.aceita = 'N'
        self.data_emissao = None
        self.codigo_juros_mora = 0
        self.data_juros_mora = 0
        self.valor_juros_mora = 0
        self.cod_desconto1 = 0
        self.data_desconto1 = 0
        self.valor_desconto1 = 0
        self.valor_IOF = 0
        self.valor_abatimento = 0
        self.identificacao_titulo_empresa = None
        self.codigo_protesto = 0
        self.dias_protesto = 0
        self.codigo_baixa = None
        self.dias_baixa = 0
        self.codigo_moeda = 0
        self.numero_contrato = 0

        self.tipo_inscricaoQ = None
        self.numero_inscricaoQ = None
        self.nomeQ = None
        self.enderecoQ = None
        self.bairroQ = None
        self.cepQ = None
        self.sufixo_cepQ = None
        self.cidadeQ = None
        self.ufQ = None
        self.tipo_inscricao_sacador = None
        self.numero_inscricao_sacador = None
        self.nome_sacador = None
        self.codigo_compensacao = 0

        self.cod_desconto2 = 0
        self.data_desconto2 = 0
        self.valor_desconto2 = 0
        self.cod_desconto3 = 0
        self.data_desconto3 = 0
        self.valor_desconto3 = 0
        self.cod_multa = 0
        self.data_multa = 0
        self.valor_multa = 0
        self.info_sacado = ''
        self.mensagem3 = ''
        self.mensagem4 = ''
        self.codigo_ocorrencia_sacado = 0
        self.cod_banco_debito = 0
        self.cod_agencia_debito = 0
        self.cod_agencia_debito_dv = ''
        self.cod_conta_debito = 0
        self.cod_conta_debito_dv = ''
        self.dv_debito = ''
        self.aviso_debito = 0

        self.tipo_registro_TL = 5
        self.qtd_registro_lote = None

        self.qtd_lote_arquivo = None
        self.qtd_registro_arquivo = None
        self.qtd_conta = 0

    def sequencia(self, nome):
        seq = 1
        lista = os.listdir(self.path)
        for l in lista:
            if l.startswith(nome):
                seq += 1
        return nome + '_{0}.rem'.format(seq)

    def gera_header_arquivo(self):
        self.data_geracao = data_now = datetime.now().strftime('%d%m%y')
        self.hora_geracao = hora_now = datetime.now().strftime('%H%M%S')
        nome = 'CNAB240_{0}_{1}_{2}'.format(self.agencia, self.numero_conta, data_now)
        nome = self.sequencia(nome)
        self.nome_arquivo = nome
        f = open(os.path.join(self.path, nome), 'w')
        string_hearder = '{0:0>3}{1:0>4}{2}{3: >9}{4}{5:0>14}{6: >9}{7: >4}{8: >2}{9: >3}{10: >2}{11:0>5}{12}{13:0>12}{14}{15}{16: <30}{17: <30}{18: >10}{19}{20}{21}{22:0>6}{23:0>3}{24:0>5}{25: >20}{26: >20}' \
                         '{27: >29}\n'.format(self.codigo_banco, self.lote_servico, self.tipo_registro, '', self.tipo_inscricao, self.numero_inscricao, '', '', '', '', '', self.agencia, self.agencia_dv, self.numero_conta,
                                              self.conta_dv, self.dv, self.nome_empresa, self.nome_banco, '', self.codigo_remessa_retorno, data_now, hora_now, self.numero_sequencial, self.layout, self.densidade, '', '', '')
        f.write(string_hearder)
        f.close()

    def gera_header_lote(self):
        f = open(os.path.join(self.path, self.nome_arquivo), 'a')
        string_hearder = '{0:0>3}{1:0>4}{2}{3: >9}{4}{5:0>14}{6: >9}{7: >4}{8: >2}{9: >3}{10: >2}{11:0>5}{12}{13:0>12}{14}{15}{16: <30}{17: <30}{18: >10}{19}{20}{21}{22:0>6}{23:0>3}{24:0>5}{25: >20}{26: >20}' \
                         '{27: >29}\n'.format(self.codigo_banco, self.lote_servico, self.tipo_registro, '', self.tipo_inscricao, self.numero_inscricao, '', '', '', '', '', self.agencia, self.agencia_dv, self.numero_conta,
                                              self.conta_dv, self.dv, self.nome_empresa, self.nome_banco, '', self.codigo_remessa_retorno, data_now, hora_now, self.numero_sequencial, self.layout, self.densidade, '', '', '')
        f.write(string_hearder)
        f.close()
