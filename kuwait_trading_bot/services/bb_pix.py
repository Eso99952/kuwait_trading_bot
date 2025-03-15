import requests
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente (se você quiser usar um arquivo .env)
load_dotenv()

# Configurações do Banco do Brasil
BB_CLIENT_ID = os.getenv('BB_CLIENT_ID', 'SEU_CLIENT_ID')
BB_CLIENT_SECRET = os.getenv('BB_CLIENT_SECRET', 'SEU_CLIENT_SECRET')
BB_DEVELOPER_KEY = os.getenv('BB_DEVELOPER_KEY', 'SEU_DEVELOPER_KEY')
BB_BASE_URL = 'https://api.bb.com.br/pix/v2'

# Função para obter o token de acesso
def obter_token():
    url = 'https://oauth.bb.com.br/oauth/token'
    auth = (BB_CLIENT_ID, BB_CLIENT_SECRET)
    payload = {'grant_type': 'client_credentials'}

    response = requests.post(url, auth=auth, data=payload)
    response.raise_for_status()
    return response.json().get('access_token')

# Função para criar um Pix
def criar_pix(valor, chave_pix):
    token = obter_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'developer_application_key': BB_DEVELOPER_KEY
    }
    payload = {
        'valor': str(valor),
        'chave': chave_pix,
        'solicitacaoPagador': 'Depósito via robô KuwaitInvest'
    }
    response = requests.post(f'{BB_BASE_URL}/cob', headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

# Função para consultar Pix
def consultar_pix(txid):
    token = obter_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'developer_application_key': BB_DEVELOPER_KEY
    }
    response = requests.get(f'{BB_BASE_URL}/cob/{txid}', headers=headers)
    response.raise_for_status()
    return response.json()

# Exemplo de uso
if __name__ == "__main__":
    try:
        valor = 10.00
        chave_pix = 'seuemail@exemplo.com'
        print('Criando Pix...')
        resposta_pix = criar_pix(valor, chave_pix)
        print('Pix criado com sucesso:', resposta_pix)
    except Exception as e:
        print('Erro:', e)
