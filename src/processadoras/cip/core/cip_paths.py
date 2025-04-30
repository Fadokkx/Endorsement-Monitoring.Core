from pathlib import Path

# Correção: Removendo o src duplicado
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent  # Volta até endorsement-monitoring.core
resources_path = PROJECT_ROOT / "processadoras" / "cip" / "resources"  # Removido o src inicial

class Diretorios_Imagem:
    sem_relatorio = str(resources_path / "Sem_Resultados_Parametro_CIP.png")
    janela_relatorio = str(resources_path / "Pagina_Relatorio_CIP.png")
    ExportarBotao = str(resources_path / "Caixa_export.png")
    TipoCSV = str(resources_path / "CSV_Option.png")