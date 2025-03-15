from services.bb_pix import criar_pix, consultar_pix

from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_bot')
def start_bot():
    return "✅ Robô Iniciado com Sucesso!"

@app.route('/stop_bot')
def stop_bot():
    return "🛑 Robô Parado com Sucesso!"

@app.route('/report')
def report():
    return "📊 Relatório Gerado com Sucesso!"

if __name__ == "__main__":
    os.system("start http://127.0.0.1:5000")
    app.run(debug=True, port=5000)

