from datetime import date, timedelta, datetime

DATA_OPERACAO = date.today() - timedelta(days=3)
DATA_FIM = date.today() - timedelta(days=1)    

class variaveis_data():
    DATA_INICIAL = DATA_OPERACAO.strftime('%d%m%Y')
    DATA_FINAL = DATA_FIM.strftime('%d%m%Y')