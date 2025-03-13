import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

EMAIL_ADDRESS = "trindadeperfeita7@gmail.com"
EMAIL_PASSWORD = "qwqj hfzk mlrf lixe"
EMAIL_DESTINO = "trindadeperfeita7@gmail.com"

class ReportGenerator:
    def __init__(self):
        self.pdf_file = "data/logs/trade_report.pdf"
        self.excel_file = "data/logs/trade_report.xlsx"

    def send_email(self):
        try:
            msg = MIMEMultipart()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = EMAIL_DESTINO
            msg['Subject'] = "📈 Relatório de Trades Kuwait - Robô 100% Automático ✅"

            # Corpo do e-mail
            body = "Olá, tudo certo? 🚀\nSegue em anexo o relatório completo das operações de trading no Kuwait! 📩"
            msg.attach(MIMEText(body, 'plain'))

            # Anexar arquivos PDF e Excel
            for file in [self.pdf_file, self.excel_file]:
                attachment = open(file, "rb")
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(file)}")
                msg.attach(part)

            # Configuração do servidor SMTP
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            server.quit()

            print("✅ E-mail enviado com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao enviar e-mail: {e}")

# Teste manual
if __name__ == "__main__":
    report = ReportGenerator()
    report.send_email()
