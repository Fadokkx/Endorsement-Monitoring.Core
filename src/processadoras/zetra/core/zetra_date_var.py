import pandas as pd

TODAY = pd.Timestamp.today().date()
DATA_OPERACAO = (TODAY - pd.offsets.BDay(3)).date()
DATA_FIM = (TODAY - pd.offsets.BDay(1)).date()

class variaveis_data():
    DATA_OPERACOES = DATA_OPERACAO.strftime('%d/%m/%Y')
    DATA_FINAL = DATA_FIM.strftime('%d/%m/%Y')