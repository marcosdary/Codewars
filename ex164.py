from pathlib import Path
from string import Template
from csv import DictReader
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from smtplib import SMTP
from dotenv import load_dotenv
from os import getenv

load_dotenv()

EMAIL_HTML = Path().home() / 'Desktop' / 'Autoconsciência' / 'Individuo' / 'email_tt.html'
DESTINATARIOS_CSV = Path().home() / 'Desktop' / 'Autoconsciência' / 'Individuo' / 'destinatarios.csv'

class AberturaSmtp:
    def __init__(self, smtp_server:str, smtp_port:int) -> None:
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self._smtp = None
    def __enter__(self):
        self._smtp = SMTP(self.smtp_server, self.smtp_port)
        return self._smtp
    
    def __exit__(self, cls, excep, trace) -> bool | Exception:
        self._smtp.close()

class AberturaArquivo:
    def __init__(self, caminho_arquivo:str, operacao_arquivo:int) -> None:
        self.caminho_arquivo = caminho_arquivo
        self.operacao_arquivo = operacao_arquivo
        self._arquivo = None
    def __enter__(self):
        self._arquivo = open(self.caminho_arquivo, self.operacao_arquivo, encoding='utf-8')
        return self._arquivo
    
    def __exit__(self, cls, excep, trace) -> bool | Exception:
        self._arquivo.close()

# Dados do remetente e destinario
remetente = getenv("FROM_EMAIL", "")

# Configurações SMTP
smtp_server = getenv("SMTP_SERVER", "")
smtp_port = getenv("SMTP_PORT", "")
smtp_username = getenv("FROM_EMAIL", "")
smtp_password = getenv("EMAIL_PASSWORD", "")

with AberturaArquivo(DESTINATARIOS_CSV, 'r') as f_dest:
    colaboradores = list(DictReader(f_dest))

with AberturaArquivo(EMAIL_HTML, 'r') as f_emai:
    template = Template(f_emai.read())



for colaborador in colaboradores:
    nome_colaborador, email_colaborador = colaborador.items()
    email = template.substitute({'nome':nome_colaborador[1]})
    mime_multipart = MIMEMultipart() 
    mime_multipart['from'] = remetente
    mime_multipart['to'] = email_colaborador[1]
    mime_multipart['subject'] = 'Projeto de Expansão' 
    
    corpo_email = MIMEText(email, 'html', 'utf-8')
    mime_multipart.attach(corpo_email)
    
    with AberturaSmtp(smtp_server, smtp_port) as server:
        server.ehlo() 
        server.starttls()
        server.login(smtp_username, smtp_password) 
        server.send_message(mime_multipart) 
        print("E-mail enviado com sucesso!!!")


