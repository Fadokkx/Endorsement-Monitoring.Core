from pathlib import Path

Raiz = Path(__file__).parent.parent.parent.parent
resources_path = Raiz / "processadoras" / "asban" / "resources"

class Diretorios_Imagem:
    campo_captcha = str(resources_path / "campo_captcha.png")