from datetime import date, timedelta, datetime
import pandas as pd

class variaveis_data():
    DATA_ARQUIVO = datetime.now().strftime("%d%m%Y")
    DATA_PASTA = datetime.now().strftime("%d-%m-%Y")
    TODAY = pd.Timestamp.today().date()
    DATA_INICIO = (TODAY - pd.offsets.BDay(3)).date()
    DATA_FINAL = (TODAY - pd.offsets.BDay(1)).date()
    DATA_OPERACAO = DATA_INICIO.strftime("%d/%m/%Y")
    DATA_FIM = DATA_FINAL.strftime("%d/%m/%Y")