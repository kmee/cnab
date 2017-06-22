# -*- encoding: utf-8 -*-

import os

from datetime import datetime, timedelta

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
        self.dv = ' '
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
        self.cobranca_cedente = 14
        self.numero_carteira = None
        self.variacao_carteira = None
        self.mensagem1 = ' '
        self.mensagem2 = ' '
        self.numero_remessa_retorno = None
        self.data_gravacao = 0
        self.data_cretido = 0

        self.tipo_regP = 3
        self.sequencial_lote = 1
        self.segmentoP = 'P'
        self.cod_movimento_remessa = 1
        self.identificacao_titulo = None
        self.codigo_carteira = 1
        self.forma_cadastro = 1
        self.tipo_doc = '1'
        self.ident_emissor_boleto = 1
        self.ident_distribuicao = '1'
        self.numero_doc_cobranca = None
        self.data_vencimento = None
        self.valor = None
        self.agencia_cobranca = 0
        self.agencia_cobranca_dv = ' '
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
        self.codigo_baixa = 0
        self.dias_baixa = 0
        self.codigo_moeda = 9
        self.numero_contrato = 0

        self.tipo_inscricaoQ = None
        self.numero_inscricaoQ = None
        self.nomeQ = None
        self.enderecoQ = None
        self.bairroQ = None
        self.cepQ = None
        self.sufixo_cepQ = None
        self.cidadeQ = ''
        self.ufQ = ''
        self.tipo_inscricao_sacador = 0
        self.numero_inscricao_sacador = 0
        self.nome_sacador = ''
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
        self.info_sacado = ' '
        self.mensagem3 = ' '
        self.mensagem4 = ' '
        self.codigo_ocorrencia_sacado = 0
        self.cod_banco_debito = 0
        self.cod_agencia_debito = 0
        self.cod_agencia_debito_dv = ' '
        self.cod_conta_debito = 0
        self.cod_conta_debito_dv = ' '
        self.dv_debito = ' '
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
        self.data_geracao = data_now = datetime.now().strftime('%d%m%Y')
        self.hora_geracao = hora_now = datetime.now().strftime('%H%M%S')
        nome = 'CNAB240_{0}_{1}_{2}'.format(self.agencia, self.numero_conta, data_now)
        nome = self.sequencia(nome)
        self.nome_arquivo = nome
        f = open(os.path.join(self.path, nome), 'w')
        string_hearder = '{0:0>3}{1:0>4}{2:0>1}{3: >9}{4:0>1}{5:0>14}{6: >9}{7: >4}{8: >2}{9: >3}{10: >2}{11:0>5}{12: >1}{13:0>12}{14: >1}{15: >1}{16: <30}{17: <30}{18: >10}{19:0>1}{20:0>8}{21:0>6}{22:0>6}{23:0>3}{24:0>5}{25: >20}{26: >20}' \
                         '{27: >29}\n'.format(self.codigo_banco, self.lote_servico, self.tipo_registro, ' ', self.tipo_inscricao, self.numero_inscricao, ' ', ' ', ' ', ' ', ' ', self.agencia, self.agencia_dv, self.numero_conta,
                                              self.conta_dv, self.dv, self.nome_empresa, self.nome_banco, ' ', self.codigo_remessa_retorno, data_now, hora_now, self.numero_sequencial, self.layout, self.densidade, ' ', ' ', ' ')
        f.write(string_hearder)
        f.close()

    def gera_header_lote(self):
        f = open(os.path.join(self.path, self.nome_arquivo), 'a')
        string_hearder_lote = '{0:0>3}{1:0>4}{2:0>1}{3: >1}{4:0>2}{5: >2}{6:0>3}{7: >1}{8:0>1}{9:0>15}{10:0>9}{11:0>4}{12:0>2}{13:0>3}{14: >2}{15:0>5}{16: >1}{17:0>12}{18: >1}{19: >1}{20: <30}{21: <40}{22: <40}{23:0>8}{24:0>8}{25:0>8}' \
                         '{26: >33}\n'.format(self.codigo_banco, self.lote, self.tipo_reg, self.tipo_operador, self.tipo_servico, '', self.layout_lote, ' ', self.tipo_inscricao, self.numero_inscricao, self.numero_convenio,
                                              self.cobranca_cedente, self.numero_carteira, self.variacao_carteira, ' ', self.agencia, self.agencia_dv, self.numero_conta, self.conta_dv, self.dv, self.nome_empresa,
                                              self.mensagem1, self.mensagem2, self.numero_remessa_retorno, self.data_gravacao, self.data_cretido, ' ')
        f.write(string_hearder_lote)
        f.close()

    def gera_segmento_p(self):
        f = open(os.path.join(self.path, self.nome_arquivo), 'a')
        string_segmento_p = '{0:0>3}{1:0>4}{2:0>1}{3:0>5}{4: >1}{5: >1}{6:0>2}{7:0>5}{8: >1}{9:0>12}{10: >1}{11: >1}{12: <20}{13:0>1}{14:0>1}{15: >1}{16:0>1}{17: >1}{18: <15}{19:0>8}{20:0>15}{21:0>5}{22: >1}{23:0>2}{24: >1}{25:0>8}' \
                         '{26:0>1}{27:0>8}{28:0>15}{29:0>1}{30:0>8}{31:0>15}{32:0>15}{33:0>15}{34: <25}{35:0>1}{36:0>2}{37:0>1}{38: >3}{39:0>2}{40:0>10}' \
                              '{41: >1}\n'.format(self.codigo_banco, self.lote, self.tipo_regP, self.sequencial_lote, self.segmentoP, ' ', self.cod_movimento_remessa, self.agencia, self.agencia_dv, self.numero_conta, self.conta_dv,
                                              self.dv, self.identificacao_titulo, self.codigo_carteira,self.forma_cadastro, self.tipo_doc, self.ident_emissor_boleto, self.ident_distribuicao, self.numero_doc_cobranca, self.data_vencimento,
                                              '{:.2f}'.format(self.valor).replace('.', ''), self.agencia_cobranca, self.agencia_cobranca_dv, self.especie, self.aceita, self.data_emissao, self.codigo_juros_mora, self.data_juros_mora,
                                              '{:.2f}'.format(self.valor_juros_mora).replace('.', ''), self.cod_desconto1, self.data_desconto1, '{:.2f}'.format(self.valor_desconto1).replace('.', ''),
                                              '{:.2f}'.format(self.valor_IOF).replace('.', ''), '{:.2f}'.format(self.valor_abatimento).replace('.', ''),
                                              self.identificacao_titulo_empresa, self.codigo_protesto, self.dias_protesto, self.codigo_baixa, self.dias_baixa, self.codigo_moeda, self.numero_contrato, ' ')
        f.write(string_segmento_p)
        f.close()

    def gera_segmento_q(self):
        f = open(os.path.join(self.path, self.nome_arquivo), 'a')
        string_segmento_q = '{0:0>3}{1:0>4}{2:0>1}{3:0>5}{4: >1}{5: >1}{6:0>2}{7:0>1}{8:0>15}{9: <40}{10: <40}{11: <15}{12:0>5}{13:0>3}{14: <15}{15: >2}{16:0>1}{17:0>15}{18: <40}{19:0>3}{20: >20}' \
                              '{21: >8}\n'.format(self.codigo_banco, self.lote, self.tipo_regP, self.sequencial_lote+1, 'Q', ' ', self.cod_movimento_remessa, self.tipo_inscricaoQ, self.numero_inscricaoQ, self.nomeQ, self.enderecoQ, self.bairroQ,
                                              self.cepQ, self.sufixo_cepQ, self.cidadeQ,self.ufQ, self.tipo_inscricao_sacador, self.numero_inscricao_sacador, self.nome_sacador, self.codigo_compensacao, ' ', ' ')
        f.write(string_segmento_q)
        f.close()

    def gera_segmento_r(self):
        f = open(os.path.join(self.path, self.nome_arquivo), 'a')
        string_segmento_r = '{0:0>3}{1:0>4}{2:0>1}{3:0>5}{4: >1}{5: >1}{6:0>2}{7:0>1}{8:0>8}{9:0>15}{10:0>1}{11:0>8}{12:0>15}{13: >1}{14:0>8}{15:0>15}{16: >10}{17: <40}{18: <40}{19: >20}{20:0>8}{21:0>3}{22:0>5}{23: >1}{24:0>12}{25: >1}{26: >1}{27:0>1}' \
                              '{28: >9}\n'.format(self.codigo_banco, self.lote, self.tipo_regP, self.sequencial_lote+2, 'R', ' ', self.cod_movimento_remessa, self.cod_desconto2, self.data_desconto2,
                                                  '{:.2f}'.format(self.valor_desconto2).replace('.', ''), self.cod_desconto3, self.data_desconto3, '{:.2f}'.format(self.valor_desconto3).replace('.', ''), self.cod_multa, self.data_multa,
                                                  '{:.2f}'.format(self.valor_multa).replace('.', ''), self.info_sacado, self.mensagem3, self.mensagem4, ' ', self.codigo_ocorrencia_sacado, self.cod_banco_debito, self.cod_agencia_debito,
                                                  self.cod_agencia_debito_dv, self.cod_conta_debito, self.cod_conta_debito_dv, self.dv_debito, self.aviso_debito, ' ')
        f.write(string_segmento_r)
        f.close()

    def gera_trailer_lote(self):
        f = open(os.path.join(self.path, self.nome_arquivo), 'a')
        string_segmento_q = '{0:0>3}{1:0>4}{2:0>1}{3: >9}{4:0>6}{5: >217}\n'.format(self.codigo_banco, self.lote, self.tipo_registro_TL, ' ', self.qtd_registro_lote, ' ')
        f.write(string_segmento_q)
        f.close()

    def gera_trailer_arquivo(self):
        f = open(os.path.join(self.path, self.nome_arquivo), 'a')
        string_segmento_q = '{0:0>3}{1:0>4}{2:0>1}{3: >9}{4:0>6}{5:0>6}{6:0>6}{7: >205}\n'.format(self.codigo_banco, 9999, 9, ' ', self.qtd_lote_arquivo, self.qtd_registro_arquivo, self.qtd_conta, ' ')
        f.write(string_segmento_q)
        f.close()

teste_remessa = GeraCNAB240(os.getcwd(), 6958, 9904)
# header_arquivo
teste_remessa.tipo_inscricao = 2
teste_remessa.numero_inscricao = 19686471000123
teste_remessa.agencia_dv = '2'
teste_remessa.nome_empresa = 'U.M. TECNOLOGIA LTDA EPP'
teste_remessa.layout = 80
# header_lote
teste_remessa.numero_convenio = 2751668
teste_remessa.numero_carteira = 17
teste_remessa.variacao_carteira = 19
teste_remessa.numero_remessa_retorno = 1
teste_remessa.data_gravacao = datetime.now().strftime('%d%m%Y')
# segmento_p
teste_remessa.identificacao_titulo = '{0}{1:0>10}'.format(teste_remessa.numero_convenio, 1)
teste_remessa.numero_doc_cobranca = '2'
teste_remessa.data_vencimento = (datetime.now() + timedelta(5)).strftime('%d%m%Y')
teste_remessa.valor = 1.0
teste_remessa.especie = 18
teste_remessa.data_emissao = datetime.now().strftime('%d%m%Y')
teste_remessa.identificacao_titulo_empresa = 10
# segmento_q
teste_remessa.tipo_inscricaoQ = 1
teste_remessa.numero_inscricaoQ = 36517608800
teste_remessa.nomeQ = 'THIAGO GOMES FREITAS'
teste_remessa.enderecoQ = 'RUA TOTTONI, 212'
teste_remessa.bairroQ = 'JD ORIENTE'
teste_remessa.cepQ = 12236
teste_remessa.sufixo_cepQ = 020
teste_remessa.cidadeQ = 'SJC'
teste_remessa.ufQ = 'SP'
# segmento_r

# trailer_lote
teste_remessa.qtd_registro_lote = 5
# trailer_arquivo
teste_remessa.qtd_lote_arquivo = 1
teste_remessa.qtd_registro_arquivo = 7

teste_remessa.gera_header_arquivo()
teste_remessa.gera_header_lote()
teste_remessa.gera_segmento_p()
teste_remessa.gera_segmento_q()
teste_remessa.gera_segmento_r()
teste_remessa.gera_trailer_lote()
teste_remessa.gera_trailer_arquivo()
