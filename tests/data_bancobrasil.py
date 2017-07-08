
from __future__ import division, print_function, unicode_literals

import os
import codecs
from decimal import Decimal

TESTS_DIRPATH = os.path.abspath(os.path.dirname(__file__))
ARQS_DIRPATH = os.path.join(TESTS_DIRPATH, 'arquivos')


def get_banco_brasil_data_from_dict():
    data = dict()

    header = {
        'controle_banco': 1,
        'arquivo_data_de_geracao': 12606201,
        'arquivo_densidade': 0,
        'arquivo_hora_de_geracao': 700000,
        'arquivo_layout': 103,
        'arquivo_sequencia': 0,
        'cedente_agencia': 1234,
        'cedente_agencia_dv': '1',
        'cedente_conta': 333333,
        'cedente_conta_dv': '0',
        'cedente_convenio': '0001234567891',
        'cedente_agencia_conta_dv': '',
        'cedente_inscricao_numero': 23130935000198,
        'cedente_inscricao_tipo': 2,
        'cedente_nome': "KMEE INFORMATICA LTDA",
        'controle_lote': 0,
        'controle_registro': 0,
        'nome_do_banco': 'BANCO DO BRASIL',
        'reservado_banco': '0',
        'reservado_empresa': 'EMPRESA 100',
        'vazio1': '',
        'vazio3': '',
        'vazio4': 'CSP000',
    }

    pagamentos = []

    pagamento_1 = {
        'aviso_ao_favorecido': 0,
        'codigo_finalidade_complementar': '',
        'codigo_finalidade_doc': '',
        'codigo_finalidade_ted': '',
        'controle_banco': 1,
        'controle_lote': 1,
        'controle_registro': 3,
        'credito_data_pagamento': 30062017,
        'credito_data_real': '',
        'credito_moeda_quantidade': Decimal('0.00000'),
        'credito_moeda_tipo': 'BRL',
        'credito_nosso_numero': '',
        'credito_seu_numero': '000133 06/2017 A',
        'credito_valor_pagamento': Decimal('6121.36'),
        'credito_valor_real': '',
        'favorecido_agencia': 4444,
        'favorecido_agencia_dv': '4',
        'favorecido_banco': 1,
        'favorecido_camara': 0,
        'favorecido_conta': 54321,
        'favorecido_conta_dv': '0',
        'favorecido_dv': ' ',
        'favorecido_nome': 'LUIS FELIPE MILEO',
        'ocorrencias': '',
        'outras_informacoes': '',
        'servico_codigo_movimento': 0,
        'servico_tipo_movimento': 0,
        'aviso': '0',
        'cod_documento_favorecido': '',
        'codigo_ispb': '0',
        'codigo_ug_centralizadora': '0',
        'favorecido_cep': 37500,
        'favorecido_cep_complemento': '150',
        'favorecido_endereco_bairro': 'CENTRO',
        'favorecido_endereco_cidade': 'ITAJUBA',
        'favorecido_endereco_complemento': '',
        'favorecido_endereco_num': 0,
        'favorecido_endereco_rua': 'RUA DOS FERROVIARIOS',
        'favorecido_estado': 'MG',
        'favorecido_num_inscricao': 33333333333,
        'favorecido_tipo_inscricao': 1,
        'pagamento_abatimento': Decimal('0.00'),
        'pagamento_desconto': Decimal('0.00'),
        'pagamento_mora': Decimal('0.00'),
        'pagamento_multa': Decimal('0.00'),
        'pagamento_valor_documento': Decimal('0.00'),
        'pagamento_vencimento': 0,
    }

    pagamento_2 = {
        'aviso_ao_favorecido': 0,
        'codigo_finalidade_complementar': '',
        'codigo_finalidade_doc': '',
        'codigo_finalidade_ted': '',
        'controle_banco': 1,
        'controle_lote': 1,
        'controle_registro': 3,
        'credito_data_pagamento': 30062017,
        'credito_data_real': '',
        'credito_moeda_quantidade': Decimal('0.00000'),
        'credito_moeda_tipo': 'BRL',
        'credito_nosso_numero': '',
        'credito_seu_numero': '000133 06/2017 A',
        'credito_valor_pagamento': Decimal('6121.36'),
        'credito_valor_real': '',
        'favorecido_agencia': 4444,
        'favorecido_agencia_dv': '4',
        'favorecido_banco': 1,
        'favorecido_camara': 0,
        'favorecido_conta': 54321,
        'favorecido_conta_dv': '0',
        'favorecido_dv': ' ',
        'favorecido_nome': 'HENDRIX COSTA',
        'ocorrencias': '',
        'outras_informacoes': '',
        'servico_codigo_movimento': 0,
        'servico_tipo_movimento': 0,
        'aviso': '0',
        'cod_documento_favorecido': '',
        'codigo_ispb': '0',
        'codigo_ug_centralizadora': '0',
        'favorecido_cep': 37500,
        'favorecido_cep_complemento': '124',
        'favorecido_endereco_bairro': 'CENTRO',
        'favorecido_endereco_cidade': 'ITAJUBA',
        'favorecido_endereco_complemento': '',
        'favorecido_endereco_num': 0,
        'favorecido_endereco_rua': 'av 3 de abril',
        'favorecido_estado': 'MG',
        'favorecido_num_inscricao': 33333333333,
        'favorecido_tipo_inscricao': 1,
        'pagamento_abatimento': Decimal('0.00'),
        'pagamento_desconto': Decimal('0.00'),
        'pagamento_mora': Decimal('0.00'),
        'pagamento_multa': Decimal('0.00'),
        'pagamento_valor_documento': Decimal('0.00'),
        'pagamento_vencimento': 0,
    }

    pagamentos.append(pagamento_1)
    pagamentos.append(pagamento_2)

    data['header'] = header
    data['pagamento'] = pagamentos

    return data


def get_banco_brasil_file_remessa():
    arquivo_remessa = codecs.open(
        os.path.join(ARQS_DIRPATH,
                     'pagamento_dict.banco_brasil.rem'), encoding='ascii')
    arquivo_data = arquivo_remessa.read()
    arquivo_remessa.close()
    return arquivo_data
