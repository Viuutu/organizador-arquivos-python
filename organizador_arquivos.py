import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organizar_pasta(caminho):
    MAPA_EXTENSOES = {
        "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
        "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
        "Compactados": [".zip", ".rar"]
    }

    arquivos_movidos = 0
    for arquivo in os.listdir(caminho):
        nome, extensao = os.path.splitext(arquivo)
        for pasta, extensoes in MAPA_EXTENSOES.items():
            if extensao.lower() in extensoes:
                pasta_destino = os.path.join(caminho, pasta)
                os.makedirs(pasta_destino, exist_ok=True)
                shutil.move(os.path.join(caminho, arquivo), os.path.join(pasta_destino, arquivo))
                arquivos_movidos += 1
    return arquivos_movidos

def selecionar_e_rodar():
    caminho = filedialog.askdirectory()
    if caminho:
        total = organizar_pasta(caminho)
        messagebox.showinfo("Sucesso", f"Organização concluída! {total} arquivos movidos.")

# Configuração da Janela
app = tk.Tk()
app.title("Organizador de Arquivos")
app.geometry("300x150")

label = tk.Label(app, text="Clique no botão para organizar uma pasta")
label.pack(pady=20)

botao = tk.Button(app, text="Selecionar Pasta", command=selecionar_e_rodar, bg="#4CAF50", fg="white")
botao.pack(pady=10)

app.mainloop()
