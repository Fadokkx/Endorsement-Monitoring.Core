from selenium.webdriver.common.by import By

class CheckBoxes():
    #Selecionar Matricula
    MATRICULA =(By.NAME,"campos:listCamposServidor:6:column:0:checkCampos") #(By.XPATH,"/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[1]/tbody/tr[2]/td[2]/input")
    #Selecionar CPF
    CPF =(By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[1]/tbody/tr[3]/td[2]/input")
    #Selecionar Nome 
    NOME =(By.XPATH,"/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[1]/tbody/tr[7]/td[1]/input")
    #Selcionar Nome reduzido do Órgão
    NOME_REDUZ_ORG =(By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[1]/tbody/tr[6]/td[1]/input")
    #Selecionar Descrição da espécie
    DESCRICAO =(By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[3]/tbody/tr[3]/td[1]/input")
    #Selecionar Número da averbação
    AVERB_NUM = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[3]/tbody/tr[6]/td[1]/input")
    #Selecionar Número do contrato
    CONTRACT_NUM = (By.XPATH,"/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[3]/tbody/tr[7]/td[1]/input")
    #Selecionar situação da averbação
    AVERB_SIT = (By.XPATH,"/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[3]/tbody/tr[9]/td[1]/input")
    #Selecionar Qtde de Parcela
    QUANT_PARCELAS = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[3]/tbody/tr[11]/td[1]/input")
    #Selecionar Valor da Parcela
    VALOR_PRCL = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[3]/tbody/tr[12]/td[1]/input")
    #Selecionar Valor liberado
    VALOR_LIB = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[3]/tbody/tr[3]/td[2]/input")
    #Selecionar Número da última parcela processada
    LAST_PRCL = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[3]/tbody/tr[7]/td[2]/input")
    #Selecionar Data de início de contrato
    CONTRACT_INICIO = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[3]/tbody/tr[11]/td[2]/input")
    #Selecionar Data da inclusão da averbação
    DATA_INCLUSAO_AVERB = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[3]/tbody/tr[13]/td[2]/input")
    