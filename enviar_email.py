import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def enviar_email(destinatario, assunto, corpo):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  

    email_origem = 'codettescompany@gmail.com' # email do codettes
    senha = 'qczp mmkg lcij aicf' # senha do email do codettes

    msg = MIMEMultipart()
    msg['From'] = email_origem
    msg['To'] = destinatario
    msg['Subject'] = assunto

    msg.attach(MIMEText(corpo, 'html'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Inicia a conexão TLS
        server.login(email_origem, senha)
        server.sendmail(email_origem, destinatario, msg.as_string())
        server.quit()
        print('Email enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar email: {str(e)}')

destinatario = ["candidohdiego@gmail.com", "aaamabili@gmail.com", "izabelly.mucholowskiribeiro@gmail.com", "camilyalbres@gmail.com","daniela.sl2f4@gmail.com"] # emails para enviar
assunto = 'Codettes'
anexo_path = 'newsletter-ready.html'

def read_md_to_string(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

corpo = read_md_to_string(anexo_path)

for email in destinatario:
    enviar_email(email, assunto, corpo)
