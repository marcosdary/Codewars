# Bibliotecas Utilizandas pelo programa
from random import randint
from pathlib import Path
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from smtplib import SMTP
from dotenv import load_dotenv
from os import getenv

load_dotenv()

# Caminho do corpo do email e Código de verificação feito randomicamente
CODIGO_VERIFICACAO = randint(100_000, 999_999)
CODIGO_VERIFICACAO_HTML = Path().home() / 'Desktop' / 'Autoconsciência' / 'Individuo' / 'codigo_verificacao.html'

# Dados do remetente e destinario
REMETENTE = getenv("FROM_EMAIL", "")

# Configurações SMTP
SMTP_SERVER = getenv("SMTP_SERVER", "")
SMTP_PORT = getenv("SMTP_PORT", "")
SMTP_USERNAME = getenv("FROM_EMAIL", "")
SMTP_PASSWORD = getenv("EMAIL_PASSWORD", "")

# Classe para conexão com o smtp
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

# Classe para abrir o arquivo html
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

class EnviarEmail:
    def __init__(self, nome:str, email:str) -> None:
        self.nome = nome
        self.email = email

    def enviar_email(self):
        with AberturaArquivo(CODIGO_VERIFICACAO_HTML, 'r') as f_emai:
            TEMPLATE = Template(f_emai.read())
            EMAIL = TEMPLATE.substitute({'nome': self.nome, 'codigo': CODIGO_VERIFICACAO})
        mime_multipart = MIMEMultipart() 
        mime_multipart['from'] = REMETENTE
        mime_multipart['to'] = self.email
        mime_multipart['subject'] = 'CÓDIGO DE VERIFICAÇÃO' 
        
        corpo_email = MIMEText(EMAIL, 'html', 'utf-8')
        mime_multipart.attach(corpo_email)

        with AberturaSmtp(SMTP_SERVER, SMTP_PORT) as server:
            server.ehlo() 
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD) 
            server.send_message(mime_multipart) 
            return "E-mail enviado com sucesso!!!"

# Interface principal existente
print("--------------------------------------------------------")
print("                      Olá Colaborador!                  ")
print("                Seja bem-vindo à nossa tela inicial!   ")
print("--------------------------------------------------------")
print("\nPor favor, insira seu nome e e-mail:\n")

# Coletando informações do usuário
nome = input("Nome: ").strip()
email = input("Email: ").strip()

# Envio do código de verificação
enviar_codigo_verificacao = EnviarEmail(nome, email)
enviar_codigo_verificacao.enviar_email()

print("--------------------------------------------------------")
print("Enviamos um código de verificação para o seu e-mail.")
print("Por favor, insira o código abaixo:\n")

# Tentativa de validação do código
try:
    codigo = int(input("Código: ").strip())
    if codigo != CODIGO_VERIFICACAO:
        raise ValueError()
    else:
        print(f"\n\t\tBem-vindo {nome}! Tenha um ótimo trabalho.\n")
except ValueError:
    print("\n\t Código fornecido inválido. Tente novamente.\n")

print("--------------------------------------------------------")
