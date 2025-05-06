from datetime import date, timedelta, datetime
import locale

locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
class variaveis_data():
    DATA_INICIO = date.today() - timedelta(days=3)  
    DATA_FIM = date.today() - timedelta(days=1)
    DATA_OPERACOES = DATA_INICIO.strftime('%d/%m/%Y')
    DATA_ATUAL = DATA_FIM.strftime('%d/%m/%Y')

    PERIODO_ASBAN = f"{DATA_OPERACOES} - {DATA_ATUAL}"