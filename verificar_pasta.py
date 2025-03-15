import os

# Caminho da pasta que você quer verificar ou criar
folder_path = r"C:\Users\maran\Downloads\Kuwaiti\kuwait_trading_bot"

# Nome do arquivo que você quer verificar dentro da pasta (opcional)
file_name = "testar_token.py"

# Verificar se a pasta existe
if not os.path.exists(folder_path):
    print(f"A pasta não existe. Criando a pasta em: {folder_path}")
    os.makedirs(folder_path)  # Cria a pasta
else:
    print(f"A pasta já existe: {folder_path}")

# Verificar se o arquivo está na pasta
file_path = os.path.join(folder_path, file_name)
if os.path.exists(file_path):
    print(f"O arquivo '{file_name}' foi encontrado na pasta!")
else:
    print(f"O arquivo '{file_name}' NÃO foi encontrado na pasta.")
