import os

# Estrutura de diretórios que será criada
folders = [
    "web_app/templates",
    "web_app/static/css",
    "web_app/static/js",
    "bot",
    "api",
    "config"
]

# Criar as pastas
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Criar o arquivo index.html dentro de templates
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Painel do Robô Kuwaitiano</title>
</head>
<body>
    <h1>🚀 Painel do Robô Kuwaitiano</h1>
    <a href="/start_bot">▶️ Iniciar Robô</a> |
    <a href="/stop_bot">🛑 Parar Robô</a> |
    <a href="/report">📊 Gerar Relatório</a>
</body>
</html>
"""

with open("web_app/templates/index.html", "w") as f:
    f.write(html_content)

print("✅ Estrutura criada com sucesso!")
