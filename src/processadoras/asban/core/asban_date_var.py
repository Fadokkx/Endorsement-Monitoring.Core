import pandas as pd
import locale

TODAY = pd.Timestamp.today().date()
DATA_OPERACAO = (TODAY - pd.offsets.BDay(3)).date()
DATA_FIM = (TODAY - pd.offsets.BDay(1)).date()
locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

class variaveis_data():
    DATA_OPERACOES= DATA_OPERACAO.strftime('%d/%m/%Y')
    DATA_ATUAL = DATA_FIM.strftime('%d/%m/%Y')

    PERIODO_ASBAN = f"{DATA_OPERACOES} - {DATA_ATUAL}"