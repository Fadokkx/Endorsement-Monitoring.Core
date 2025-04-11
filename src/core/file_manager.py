import os
import shutil

def renomear_e_mover_arquivos(pasta_origem, pasta_destino, parametro_nome, novo_nome):
    try:
        # Criar a pasta de destino, se não existir
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
            print(f"Pasta de destino criada: {pasta_destino}")
 
        # Listar arquivos na pasta de origem
        arquivos = os.listdir(pasta_origem)
        contador = 1  # Contador para evitar nomes duplicados
 
        for arquivo in arquivos:
            caminho_origem = os.path.join(pasta_origem, arquivo)
 
            # Ignorar pastas
            if os.path.isdir(caminho_origem):
                continue
 
            # Verificar se o parâmetro está no nome do arquivo
            if parametro_nome in arquivo:
                # Criar o novo nome do arquivo
                extensao = os.path.splitext(arquivo)[1]  # Pega a extensão do arquivo
                novo_nome = f"{novo_nome}{extensao}"
                contador += 1
 
                caminho_destino = os.path.join(pasta_destino, novo_nome)
 
                # Renomear e mover o arquivo
                shutil.move(caminho_origem, caminho_destino)
                print(f"Renomeado e movido: {arquivo} -> {novo_nome}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")