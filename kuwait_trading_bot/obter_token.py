import requests
import logging

# Configuração de logs
logging.basicConfig(level=logging.INFO)

def obter_token():
    # Endpoint da API
    url = "https://oauth.bb.com.br/oauth/token"

    # Credenciais e dados da requisição
    data = {
        "grant_type": "client_credentials",
        "client_id": "eyJpZCI6IjI1YjdmZjQtOTE0MS00YTI4LTk2MjQtNzc0IiwiY29kaWdvUHVibGljYWRvciI6MCwiY29kaWdvU29mdHdhcmUiOjEyODY5Mywic2VxdWVuY2lhbEluc3RhbGFjYW8iOjF9",  # Substituir pelo seu Client ID
        "client_secret": "eyJpZCI6Ijk4NGI1NTgtNTA4Ny00N2UzIiwiY29kaWdvUHVibGljYWRvciI6MCwiY29kaWdvU29mdHdhcmUiOjEyODY5Mywic2VxdWVuY2lhbEluc3RhbGFjYW8iOjEsInNlcXVlbmNpYWxDcmVkZW5jaWFsIjoxLCJhbWJpZW50ZSI6ImhvbW9sb2dhY2FvIiwiaWF0IjoxNzQxOTU4MzY4ODM1fQ",  # Substituir pelo seu Client Secret
        "scope": "pix.read pix.write"  # Ajustar conforme a necessidade
    }

    # Cabeçalhos
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        # Fazer a requisição POST
        logging.info("Enviando a requisição para obter o token...")
        response = requests.post(url, data=data, headers=headers)

        # Tratamento para códigos de status HTTP
        if response.status_code == 200:
            logging.info("Token obtido com sucesso!")
            return response.json().get("access_token")
        elif response.status_code == 405:
            logging.error("Erro 405: Método não permitido. Verifique o método HTTP usado.")
            raise Exception("Método não permitido. O endpoint pode esperar outro método.")
        elif response.status_code == 403:
            logging.error("Erro 403: Acesso proibido. Pode haver bloqueio pelo Cloudflare.")
            raise Exception("Acesso bloqueado pelo servidor ou Cloudflare.")
        else:
            logging.error(f"Erro {response.status_code}: {response.text}")
            raise Exception(f"Erro inesperado: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        # Tratamento de erros de conexão
        logging.error(f"Erro de conexão: {str(e)}")
        raise Exception("Erro ao se conectar à API.") from e
    except Exception as e:
        # Tratamento de outros erros
        logging.error(f"Erro desconhecido: {str(e)}")
        raise

# Teste da função
if __name__ == "__main__":
    try:
        token = obter_token()
        print("Token obtido:", token)
    except Exception as e:
        print(f"Falha ao obter o token: {e}")

