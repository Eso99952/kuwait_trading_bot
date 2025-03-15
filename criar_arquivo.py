import os

# Caminho do diretório onde o arquivo será salvo
directory = r"C:\Users\maran\Downloads\Kuwaiti\kuwait_trading_bot"

# Nome do arquivo
file_name = "autenticacao_bb.py"

# Código a ser gravado no arquivo
conteudo = '''import requests

# Dados da autenticação
url_auth = "https://oauth.bb.com.br/oauth/token"
credentials = {
    "grant_type": "client_credentials",
    "client_id": "SEU_CLIENT_ID",
    "client_secret": "SEU_CLIENT_SECRET",
    "scope": "pix.read pix.write"  # Ajuste o escopo se necessário
}

# Solicitar token de acesso
response = requests.post(url_auth, data=credentials)
if response.status_code == 200:
    access_token = response.json().get("access_token")
    print("Token de Acesso:", access_token)
else:
    print("Erro ao autenticar:", response.json())
'''

# Criação do arquivo no diretório
try:
    # Verifica se o diretório existe
    if not os.path.exists(directory):
        os.makedirs(directory)  # Cria o diretório, se necessário
    
    # Caminho completo para o arquivo
    file_path = os.path.join(directory, file_name)
    
    # Grava o conteúdo no arquivo
    with open(file_path, "w") as file:
        file.write(conteudo)
    
    print(f"Arquivo {file_name} criado com sucesso em {directory}")
except Exception as e:
    print(f"Erro ao criar o arquivo: {e}")
