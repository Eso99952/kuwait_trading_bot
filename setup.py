import os

# Estrutura de pastas e arquivos do robô
directories = [
    "kuwait_trading_bot",
    "kuwait_trading_bot/web_app",
    "kuwait_trading_bot/web_app/templates",
    "kuwait_trading_bot/web_app/static",
    "kuwait_trading_bot/api",
    "kuwait_trading_bot/utils",
]

# Arquivos que serão criados
files = {
    "kuwait_trading_bot/app.py": "", # O app principal
    "kuwait_trading_bot/web_app/templates/index.html": "", # Página web
    "kuwait_trading_bot/kuwait_api.py": "", # Conexão com a bolsa do Kuwait
    "kuwait_trading_bot/config.py": "", # Configurações do robô
    "kuwait_trading_bot/utils/logger.py": "", # Sistema de logs
}

# Criar as pastas
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Criar os arquivos
for file_path, content in files.items():
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(content)

print("✅ Estrutura do robô criada com sucesso!")


