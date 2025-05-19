from pathlib import Path

Raiz = Path(__file__).parent.parent.parent.parent
resources_path = Raiz / "processadoras" / "quantumweb" / "resources"

class Diretorios_Imagem:
    aba_relatorio = str(resources_path / "opcao_rel.png")