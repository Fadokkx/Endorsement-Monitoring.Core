from pathlib import Path

Raiz = Path(__file__).parent.parent.parent.parent
resources_path = Raiz / "processadoras" / "consigtec" / "images"

class Diretorios_Imagem:
    sem_relatorio = str(resources_path / "Sem_relatorios.png")