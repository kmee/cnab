# -*- encoding: utf8 -*-

from evento import Evento
from .. import errors


class Lote(object):

    def __init__(self, banco, header=None, trailer=None):
        self.banco = banco
        self.header = header
        self.trailer = trailer
        self._codigo = None
        self.trailer.quantidade_registros = 2
        self._eventos = []

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor
        if self.header is not None:
            self.header.controle_lote = valor
        if self.trailer is not None:
            self.trailer.controle_lote = valor
        self.atualizar_codigo_eventos()

    def atualizar_codigo_eventos(self):
        for evento in self._eventos:
            evento.codigo_lote = self._codigo

    def atualizar_codigo_registros(self):
        last_id = 0
        for evento in self._eventos:
            last_id = evento.atualizar_codigo_registros(last_id)

    @property
    def eventos(self):
        return self._eventos

    def adicionar_evento(self, evento):
        if not isinstance(evento, Evento):
            raise TypeError

        self._eventos.append(evento)
        if self.trailer is not None and \
                hasattr(self.trailer, 'quantidade_registros'):
            self.trailer.quantidade_registros += len(evento)
        self.atualizar_codigo_registros()

        if self._codigo:
            self.atualizar_codigo_eventos()

    def __unicode__(self):
        if not self._eventos:
            raise errors.NenhumEventoError()

        result = []
        if self.header is not None:
            result.append(unicode(self.header))
        result.extend(unicode(evento) for evento in self._eventos)
        if self.trailer is not None:
            result.append(unicode(self.trailer))
        return '\r\n'.join(result)

    def __len__(self):
        if self.trailer is not None and \
                hasattr(self.trailer, 'quantidade_registros'):
            return self.trailer.quantidade_registros
        else:
            return len(self._eventos)
