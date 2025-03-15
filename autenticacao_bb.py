import requests

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
