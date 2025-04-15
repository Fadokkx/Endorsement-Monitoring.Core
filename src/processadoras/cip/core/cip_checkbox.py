from selenium.webdriver.remote.webdriver import WebDriver as driver
from selenium.webdriver.common.by import By

class CheckBoxes ():
    #Selecionar Matricula
    MATRICULA = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[1]/tbody/tr[2]/td[2]/input").click()
    #Selecionar CPF
    CPF = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[1]/tbody/tr[3]/td[2]/input").click()
    #Selecionar Nome 
    NOME = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[1]/tbody/tr[7]/td[1]/input").click()
    #Selcionar Nome reduzido do Órgão
    NOME_REDUZ_ORG = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[1]/tbody/tr[6]/td[1]/input").click()
    #Selecionar Descrição da espécie
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[3]/tbody/tr[3]/td[1]/input").click()
    #Selecionar Número da averbação
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[3]/tbody/tr[6]/td[1]/input").click()
    #Selecionar Número do contrato
    driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[3]/tbody/tr[7]/td[1]/input").click()
    #Selecionar situação da averbação
    driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[3]/tbody/tr[9]/td[1]/input").click()
    #Selecionar Qtde de Parcela
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[3]/tbody/tr[11]/td[1]/input").click()
    #Selecionar Valor da Parcela
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[3]/tbody/tr[12]/td[1]/input").click()
    #Selecionar Valor liberado
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[3]/tbody/tr[3]/td[2]/input").click()
    #Selecionar Número da última parcela processada
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[3]/tbody/tr[7]/td[2]/input").click()
    #Selecionar Data de início de contrato
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[3]/tbody/tr[11]/td[2]/input").click()
    #Selecionar Data da inclusão da averbação
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/div[6]/div/div[2]/table[3]/tbody/tr[13]/td[2]/input").click()
    