import os
import shutil

# Defina o caminho da pasta que você quer organizar
caminho_origem = os.path.expanduser("~/Downloads")

# Dicionário que mapeia extensões para nomes de pastas
MAPA_EXTENSOES = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Executaveis": [".exe", ".msi", ".dmg"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Videos": [".mp4", ".mkv", ".mov"]
}

def organizar():
    # Entra na pasta de origem
    for arquivo in os.listdir(caminho_origem):
        nome, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()

        # Verifica em qual categoria a extensão se encaixa
        for pasta, extensoes_suportadas in MAPA_EXTENSOES.items():
            if extensao in extensoes_suportadas:
                pasta_destino = os.path.join(caminho_origem, pasta)

                # Cria a pasta se ela não existir
                if not os.path.exists(pasta_destino):
                    os.makedirs(pasta_destino)

                # Move o arquivo
                origem_arquivo = os.path.join(caminho_origem, arquivo)
                destino_arquivo = os.path.join(pasta_destino, arquivo)

                print(f"Movendo: {arquivo} -> {pasta}")
                shutil.move(origem_arquivo, destino_arquivo)

if __name__ == "__main__":
    organizar()
    print("Organização concluída!")
