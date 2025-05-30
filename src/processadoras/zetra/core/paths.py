from pathlib import Path

Raiz = Path(__file__).parent.parent.parent.parent
resources_path = Raiz / "processadoras" / "zetra" / "resources"

class Diretorios_Imagem:
    botao = str(resources_path / "Botao_confirmar.png")