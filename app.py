import streamlit as st
import os
import shutil
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Organizador de Arquivos", page_icon="📂")

st.title("📂 Organizador de Pastas Inteligente")
st.markdown("Transforme sua bagunça em pastas organizadas com um clique.")

# Input para o caminho da pasta
caminho = st.text_input("Cole o caminho da pasta aqui (ex: C:/Users/Nome/Downloads):")

# Dicionário de Categorias
MAPA_EXTENSOES = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Compactados": [".zip", ".rar"],
    "Videos": [".mp4", ".mov", ".avi"]
}

if st.button("🚀 Organizar Agora"):
    if os.path.exists(caminho):
        arquivos_movidos = 0
        lista_arquivos = os.listdir(caminho)

        progresso = st.progress(0)

        for i, arquivo in enumerate(lista_arquivos):
            nome, extensao = os.path.splitext(arquivo)
            for pasta, extensoes in MAPA_EXTENSOES.items():
                if extensao.lower() in extensoes:
                    pasta_destino = os.path.join(caminho, pasta)
                    os.makedirs(pasta_destino, exist_ok=True)
                    shutil.move(os.path.join(caminho, arquivo), os.path.join(pasta_destino, arquivo))
                    arquivos_movidos += 1

            # Atualiza barra de progresso
            progresso.progress((i + 1) / len(lista_arquivos))

        st.success(f"Feito! {arquivos_movidos} arquivos foram organizados.")
        st.balloons() # Efeito visual legal
    else:
        st.error("Caminho não encontrado. Verifique e tente novamente.")
