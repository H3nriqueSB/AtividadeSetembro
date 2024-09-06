import customtkinter as ctk

app = ctk.CTk()  # Criar a instância da aplicação
app.geometry("300x400")  # Definir tamanho da janela

# Variáveis para armazenar o valor atual e o valor anterior
valor_atual = ""
valor_anterior = ""
operacao = ""

def exibir_numero(numero):
    global valor_atual
    valor_atual += str(numero)  # Adiciona o número ao valor atual
    texto_label.configure(text=valor_atual)  # Atualiza o Label

def definir_operacao(op):
    global valor_anterior, valor_atual, operacao
    valor_anterior = valor_atual  # Armazena o valor atual
    operacao = op  # Define a operação
    valor_atual = ""  # Limpa o valor atual

def calcular_resultado():
    global valor_atual, valor_anterior, operacao
    if operacao == "+":
        resultado = str(float(valor_anterior) + float(valor_atual))
    else:
        resultado = valor_atual  # Se não houver operação, mantém o valor atual
    texto_label.configure(text=resultado)  # Exibe o resultado
    valor_atual = resultado  # Atualiza o valor atual para o resultado

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

# Criar o botão de adição
botao_mais = ctk.CTkButton(app, height=50, width=70, text='+', fg_color='gray', corner_radius=0, command=lambda: definir_operacao('+'))
botao_mais.place(x=230, y=310)

# Criar o botão de igual
botao_igual = ctk.CTkButton(app, height=50, width=70, text='=', fg_color='gray', corner_radius=0, command=calcular_resultado)
botao_igual.place(x=230, y=240)

app.mainloop()
