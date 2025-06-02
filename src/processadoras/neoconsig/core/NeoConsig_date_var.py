from datetime import date, timedelta, datetime
import locale

locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

DATA_FIM = date.today() - timedelta(days=1)    
INFO_DATA = date.today().strftime('%B')
DATA_COMPLETA = datetime.now() 

class variaveis_data():
    DIA_ATUAL = date.today().day
    MES_ANTERIOR = (DATA_FIM.replace(day=1) - timedelta(days=1)).strftime("%B")    
    MES_ATUAL = DATA_COMPLETA.strftime("%B")
    ANO_ANTERIOR = date.today().year - 1
    ANO_ATUAL = date.today().year
    
    # CONDICAO DIA
    if DIA_ATUAL <= 2:
        
        if MES_ATUAL == "janeiro" and DIA_ATUAL <= 2:
            MES_ATUAL = MES_ANTERIOR
            ANO_ATUAL = ANO_ANTERIOR
        
        if MES_ANTERIOR == "marÃ§o":
            MES_ANTERIOR = "marco"
            
        MES_ATUAL = MES_ANTERIOR 