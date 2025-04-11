from src.processadoras.cip.convenios.govsp import ConvenioGovSP
#from src.processadoras.zetra.convenios.nova_lima import ConvenioNovaLima
#from src.processadoras.zetra.convenios.embu import ConvenioEmbu
from typing import Dict, Type
from selenium.webdriver.remote.webdriver import WebDriver

class CipController:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.convenios: Dict[str, Type] = {
            'sobral': ConvenioGovSP,
#            'nova_lima': ConvenioNovaLima,
#            'embu': ConvenioEmbu
            # Adicione outros convênios aqui
        }