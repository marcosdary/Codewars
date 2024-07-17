from re import I, findall
texto = '''
contato@empresa.com.br
suporte_tecnico@provedor.net
vendas123@lojavirtual.com.br
newsletter@sitedenoticias.org
faleconosco@servidor.gov.br
atendimento24h@minhaempresa.com
usuario.extra@dominio.info
'''

texto_2 = '''
Agradecemos o seu interesse em nossos serviços. 
Para obter mais informações ou solicitar um orçamento, 
entre em contato conosco através do telefone (11) 98765-4321 
ou envie um e-mail para rodrigomaia@email.com. 
Nossa equipe estará à disposição para atendê-lo.
'''


for dominio in findall(r'@[a-zA-Z0-9.]{,20}', texto, flags=I):
    print(dominio[1:])
print()
print()
for dados in findall(r'\([0-9]{2}\) [0-9]{5}-[0-9]{4}|[a-zA-Z0-9]+@[a-zA-Z0-9.]{9}', texto_2, flags=I):
    print(dados)