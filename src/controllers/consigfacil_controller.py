from src.processadoras.consigfacil.convenios.campina_grande import ConvenioCampinaGrande
from src.processadoras.consigfacil.convenios.cuiaba import ConvenioCuiaba
from src.processadoras.consigfacil.convenios.ipatinga import ConvenioIpatinga
from src.processadoras.consigfacil.convenios.joao_pessoa import ConvenioJoaoPessoa
from src.processadoras.consigfacil.convenios.juazeiro_do_norte import ConvenioJuazeiro
from src.processadoras.consigfacil.convenios.maranhao import ConvenioMaranhao
from src.processadoras.consigfacil.convenios.pernambuco import ConvenioPernambuco
from src.processadoras.consigfacil.convenios.piaui import ConvenioPiaui
from src.processadoras.consigfacil.convenios.porto_velho import ConvenioPortoVelho
from src.processadoras.consigfacil.convenios.recife import ConvenioRecife
from src.processadoras.consigfacil.convenios.teresina import ConvenioTeresina
from src.core.file_manager import renomear_e_mover_arquivos as file_manager
from src.core.date_var import variaveis_data as data
from src.core.paths import caminhos as paths
from typing import Dict, Type
from selenium.webdriver.remote.webdriver import WebDriver

class ConsigFacilController():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.convenios: Dict[str, Type] = {
            'campina_grande': ConvenioCampinaGrande,
            'cuiaba': ConvenioCuiaba,
            'ipatinga': ConvenioIpatinga,
            'joao_pessoa': ConvenioJoaoPessoa,
            'juazeiro': ConvenioJuazeiro,
            'maranhao': ConvenioMaranhao,
            'pernambuco': ConvenioPernambuco,
            'piaui': ConvenioPiaui,
            'porto_velho': ConvenioPortoVelho,
            'recife': ConvenioRecife,
            'teresina': ConvenioTeresina
        }
    
    def executar_fluxo_completo(self, nome_convenio: str) -> bool:
        #Executa todo o fluxo para um convênio específico com tratamento detalhado de erros
        if nome_convenio not in self.convenios:
            raise ValueError(f"Convênio {nome_convenio} não existe")
        
        convenio = self.convenios[nome_convenio](self.driver)
        try:
            if not convenio.login():
                raise Exception("Falha no login")
            
            if not convenio.confirmacao_leitura_novidades():
                raise Exception ("Falha na Confirmação de leitura.") 
            
            if not convenio.navega_menu():
                raise Exception ("Falha na navegação do menu")
            
            if not convenio.opcoes_relatorio():
                raise Exception ("Falha ao selecionar as opções de relatório")
            
            if not convenio.baixar_relatorio():
                raise Exception ("Falha ao baixar relatório")
            
            try:
                file_manager(pasta_origem=paths.pasta_download, pasta_destino=rf"C:\Relatórios\{data.DATA_PASTA}", parametro_nome= "relatorio", novo_nome=(f"consigfacil_{nome_convenio}_{data.DATA_ARQUIVO}"))
            except Exception as e:
                print(f"{e}")
        
        except Exception as e:
            raise Exception(f"[{nome_convenio.upper()}] {str(e)}") from e
        
    def executar_todos_convenios(self, convenios_selecionados: list = None):
        """Executa vários convênios em sequência"""
        resultados = {}
        convenios = convenios_selecionados or self.convenios.keys()
        
        for nome in convenios:
            try:
                sucesso = self.executar_fluxo_completo(nome)
                resultados[nome] = {
                    'status': 'Sucesso' if sucesso else 'Falha',
                    'erro': None
                }
            except Exception as e:
                resultados[nome] = {
                    'status': 'Erro crítico',
                    'erro': str(e)
                }
        return resultados