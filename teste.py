import customtkinter as ctk

app = ctk.CTk()  # Criar a instância da aplicação
app.geometry("300x400")  # Definir tamanho da janela

# Função que exibe o número no topo da tela
# def exibir_numero(numero):
#     texto_label.configure(text=str(numero))  # Atualiza o Label com o número clicado

def exibir_numero(numero):
    texto_atual = texto_label.cget("text")  # Obter o texto atual do Label
    texto_label.configure(text=texto_atual + str(numero))  # Concatenar o novo número

# Criar o widget de texto (label) com texto inicial vazio
texto_label = ctk.CTkLabel(app, text="", font=("Arial", 24))
texto_label.pack(pady=20)  # Posicionar no topo com espaçamento vertical

# Criar os botões 7, 8 e 9
sete = ctk.CTkButton(app, height=50, width=70, text='7', fg_color='gray', corner_radius=0, command=lambda: exibir_numero(7))
sete.place(x=5, y=310)

oito = ctk.CTkButton(app, height=50, width=70, text='8', fg_color='gray', corner_radius=0, command=lambda: exibir_numero(8))
oito.place(x=80, y=310)

nove = ctk.CTkButton(app, height=50, width=70, text='9', fg_color='gray', corner_radius=0, command=lambda: exibir_numero(9))
nove.place(x=155, y=310)

app.mainloop()

app.mainloop()
