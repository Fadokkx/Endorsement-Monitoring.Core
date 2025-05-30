from pathlib import Path

Raiz = Path(__file__).parent.parent.parent.parent
resources_path = Raiz / "processadoras" / "consigfacil" / "resources"

class Diretorios_Imagem:
    sem_relatorio = str(resources_path / "Sem_relatorio.png")
    erro_url = str(resources_path / "Erro_url.png")