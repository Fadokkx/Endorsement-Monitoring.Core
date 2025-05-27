from pathlib import Path

Raiz = Path(__file__).parent.parent.parent.parent
resources_path = Raiz / "processadoras" / "proconsig" / "resources"

class Diretorios_Imagem:
    aba_relatorio = str(resources_path / "aba_consignacoes.png")
    opcao_consignacao =str(resources_path / "pesquisa_consignacao.png")