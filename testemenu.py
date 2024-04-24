import tkinter as tk
import subprocess

def iniciar_hover(event):
    iniciar_label.config(image=iniciar_hover_img)

def iniciar_leave(event):
    iniciar_label.config(image=iniciar_img)

def sair_hover(event):
    sair_label.config(image=sair_hover_img)

def sair_leave(event):
    sair_label.config(image=sair_img)
    
def iniciar():
    # Execute o arquivo Python desejado
    subprocess.run(["python", "C:/Users/RA00340509/Documents/VERSAO FINAL-20240424T113030Z-001/VERSAO FINAL/trabalho_final_otimização.py"])

def sair():
    root.destroy()

root = tk.Tk()
root.title("Menu")
root.geometry("1920x1080")

# Carregar imagens
background_img = tk.PhotoImage(file="C:/Users/RA00340509/Documents/VERSAO FINAL-20240424T113030Z-001/VERSAO FINAL/Visual/f.png")
iniciar_img = tk.PhotoImage(file="C:/Users/RA00340509/Documents/VERSAO FINAL-20240424T113030Z-001/VERSAO FINAL/Visual/botao-iniciar-idle.png")
iniciar_hover_img = tk.PhotoImage(file="C:/Users/RA00340509/Documents/VERSAO FINAL-20240424T113030Z-001/VERSAO FINAL/Visual/botao-iniciar-selecionado.png")
sair_img = tk.PhotoImage(file="C:/Users/RA00340509/Documents/VERSAO FINAL-20240424T113030Z-001/VERSAO FINAL/Visual/botao-sair-idle.png")
sair_hover_img = tk.PhotoImage(file="C:/Users/RA00340509/Documents/VERSAO FINAL-20240424T113030Z-001/VERSAO FINAL/Visual/botao-sair-selecionado.png")

# Adicionar imagem de fundo
background_label = tk.Label(root, image=background_img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Adicionar botões
iniciar_label = tk.Label(root, image=iniciar_img, bd=0, highlightthickness=0, bg="transparent")
iniciar_label.place(x=700, y=500)
iniciar_label.bind("<Enter>", iniciar_hover)
iniciar_label.bind("<Leave>", iniciar_leave)
iniciar_label.bind("<Button-1>", lambda event: iniciar())

sair_label = tk.Label(root, image=sair_img, bd=0, highlightthickness=0)
sair_label.place(x=850, y=600)
sair_label.bind("<Enter>", sair_hover)
sair_label.bind("<Leave>", sair_leave)
sair_label.bind("<Button-1>", lambda event: sair())

root.mainloop()
