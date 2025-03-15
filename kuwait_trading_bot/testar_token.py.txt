from obter_token import obter_token

try:
    token = obter_token()
    print("Token obtido:", token)
except Exception as e:
    print("Erro ao obter o token:", e)
