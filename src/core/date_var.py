from datetime import date, timedelta, datetime

DATA_OPERACAO = date.today() - timedelta(days=3)
DATA_FIM = datetime.now() - timedelta(days=1)    

class variaveis_data():
    DATA_OPERACOES = DATA_OPERACAO.strftime('%d/%m/%Y')
    DATA_FINAL = DATA_FIM.strftime('%d/%m/%Y')