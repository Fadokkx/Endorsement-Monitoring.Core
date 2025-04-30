from pathlib import Path

Raiz = Path(__file__).parent.parent.parent.parent
resources_path = Raiz / "processadoras" / "cip" / "resources"

class Diretorios_Imagem:
    sem_relatorio = str(resources_path / "Sem_Relatorios_CIP.png")
    janela_relatorio = str(resources_path / "Pagina_Relatorio_CIP.png")
    ExportarBotao = str(resources_path / "Caixa_export.png")
    TipoCSV = str(resources_path / "CSV_Option.png")