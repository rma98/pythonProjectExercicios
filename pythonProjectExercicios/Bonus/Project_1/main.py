import pandas as pd
from twilio.rest import Client

# Instalações
# pandas
# openpyxl
# twilio

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACec09a840289c09eea5555543eaebdb88'
auth_token = '74109507c3dc567b5fd56cfcb6e03d40'
client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir os seis arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        #print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages \
            .create(
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}',
            from_='++13236161381',
            to='+5581971168633'
        )
        print(message.sid)

# Para cada arquivo:

# verificar se algum valor na coluna de vendas daquele arquivo é maior que 55.000

# Se for maior que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendendor

# Caso não seja maior que 55.000 não quero fazer nada
