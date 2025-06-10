import os
import shutil
import csv
import re
import zipfile
import pandas as pd
from datetime import datetime
from src.core.aws_config import ConfigAws as CA, Paths as Paths_S3
from src.core.date_var import variaveis_data as Data
from src.core.paths import caminhos as path

class data_management:
    
    def upload_s3(caminho_arquivo_local: str, nome_destino_s3: str):
        bucket = Paths_S3.Bucket
        try:
            CA.Aws_client.upload_file(caminho_arquivo_local, bucket, nome_destino_s3)
        except Exception as e:
            print(f"Erro ao fazer upload para o S3: {e}")
            raise
    
    def remove_arquivo_consigfacil():

        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

        padrao = re.compile(r"relatorio \(\d+\)\.csv")

        for arquivo in os.listdir(downloads_path):
            if padrao.fullmatch(arquivo):
                caminho_arquivo = os.path.join(downloads_path, arquivo)
                try:
                    os.remove(caminho_arquivo)
                except Exception as e:
                    print(f"Erro ao remover o arquivo '{arquivo}': {e}")

    def extracao_zetra(pasta_download: str, nome_convenio: str, data_arquivo: str) -> str:
        try:
            nome_zip = f"zetra_{nome_convenio}_{data_arquivo}.zip"
            caminho_zip = os.path.join(pasta_download, nome_zip)

            if not os.path.isfile(caminho_zip):
                raise FileNotFoundError(f"Arquivo ZIP não encontrado: {caminho_zip}")

            with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
                arquivos_zip = zip_ref.namelist()
                arquivo_inclusao = next((f for f in arquivos_zip if f.upper().startswith("INCLUSAO_")), None)

                if not arquivo_inclusao:
                    raise FileNotFoundError("Nenhum arquivo que começa com 'INCLUSAO_' foi encontrado no ZIP.")

                zip_ref.extract(arquivo_inclusao, path=pasta_download)

                caminho_extraido = os.path.join(pasta_download, arquivo_inclusao)

                extensao = os.path.splitext(arquivo_inclusao)[1]
                novo_nome = f"zetra_{nome_convenio}_{data_arquivo}{extensao}"
                caminho_renomeado = os.path.join(pasta_download, novo_nome)

                os.rename(caminho_extraido, caminho_renomeado)
                print(f"Arquivo extraído e renomeado: {caminho_renomeado}")

                return caminho_renomeado

        except Exception as e:
            print(f"Erro {e}")
            raise

    def renomear_e_mover_arquivos(pasta_origem, pasta_destino, parametro_nome, novo_nome):
        try:
            # Criar pasta destino se não existir
            os.makedirs(pasta_destino, exist_ok=True)

            arquivos = os.listdir(pasta_origem)

            for arquivo in arquivos:
                caminho_origem = os.path.join(pasta_origem, arquivo)

                if os.path.isdir(caminho_origem):
                    continue

                if parametro_nome in arquivo:
                    extensao = os.path.splitext(arquivo)[1]
                    novo_nome_completo = f"{novo_nome}{extensao}"
                    caminho_destino = os.path.join(pasta_destino, novo_nome_completo)

                    shutil.move(caminho_origem, caminho_destino)
                    print(f"Renomeado e movido: {arquivo} → {novo_nome_completo}")
                    return caminho_destino

            raise FileNotFoundError(f"Nenhum arquivo contendo '{parametro_nome}' foi encontrado em {pasta_origem}.")

        except Exception as e:
            print(f"Ocorreu um erro ao renomear/mover arquivos: {e}")
            raise
        
    def alteracao_neoconsig(pasta_download: str, nome_convenio: str, data_arquivo: str) -> str:
        pass
    
    def SepSafeConsig(convenio, data):
        try:
            pasta_download = os.path.join(path.pasta_download)
            arquivo_csv = f"safeconsig_{convenio}_{data}.csv"
            
            caminho_arquivo = os.path.join(pasta_download, arquivo_csv)
            
            df = pd.read_csv(caminho_arquivo, encoding="ISO-8859-1")
            df.to_csv(
            caminho_arquivo,
            sep=";",              # separador ponto-e-vírgula
            index=False,
            encoding="utf-8-sig", # compatível com Excel
            quoting=3             # 3 = csv.QUOTE_NONE → evita aspas desnecessárias
        )
            
        except Exception as e:
            print(f"Erro: {e}")