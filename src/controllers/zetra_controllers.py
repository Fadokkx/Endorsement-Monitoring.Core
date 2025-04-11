from src.processadoras.zetra.convenios.sobral import ConvenioSobral
#from src.processadoras.zetra.convenios.nova_lima import ConvenioNovaLima
#from src.processadoras.zetra.convenios.embu import ConvenioEmbu
from typing import Dict, Type
from selenium.webdriver.remote.webdriver import WebDriver

class ZetraController:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.convenios: Dict[str, Type] = {
            'sobral': ConvenioSobral,
            #'nova_lima': ConvenioNovaLima,
            #'embu': ConvenioEmbu
            # Adicione outros convênios aqui
        }

    def executar_fluxo_completo(self, nome_convenio: str) -> bool:
        """Executa todo o fluxo para um convênio específico com tratamento detalhado de erros"""
        if nome_convenio not in self.convenios:
            raise ValueError(f"Convênio {nome_convenio} não existe")
        
        convenio = self.convenios[nome_convenio](self.driver)
        
        try:
            if not convenio.login():
                raise Exception("Falha no login")
            
            if not convenio.navegar_menu():
                raise Exception("Falha na navegação do menu")
            
            if not convenio.opcoes_relatorios():
                raise Exception("Falha nas opções de relatório")
            
            if not convenio.autorizer():
                raise Exception("Falha na autorização")
            
            return True
            
        except Exception as e:
            # Adiciona o nome do convênio ao erro
            raise Exception(f"[{nome_convenio.upper()}] {str(e)}") from e

    def executar_todos_convenios(self, convenios_selecionados: list = None):
        """Executa vários convênios em sequência"""
        resultados = {}
        convenios = convenios_selecionados or self.convenios.keys()
        
        for nome in convenios:
            try:
                sucesso = self.executar_fluxo_completo(nome)
                resultados[nome] = {
                    'status': '✅ Sucesso' if sucesso else '❌ Falha',
                    'erro': None
                }
            except Exception as e:
                resultados[nome] = {
                    'status': '🔥 Erro crítico',
                    'erro': str(e)
                }
        
        return resultados