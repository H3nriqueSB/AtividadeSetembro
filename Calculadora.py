import customtkinter as ctk
from PIL import Image, ImageTk
import os

valor_atual = ""
valor_anterior = ""
operacao = ""

app = ctk.CTk()
app.geometry('320x530')
app.configure(fg_color='black')
app.title('Calculadorinator')

img_path = 'bg.png'
img = Image.open(img_path) 
background = ImageTk.PhotoImage(img)

label_img = ctk.CTkLabel(app, image=background, text='')
label_img.place(x=0, y=0)

def exibir_numero(numero):
    global valor_atual
    valor_atual += str(numero)
    display.configure(text=valor_atual) 

display = ctk.CTkLabel(app, text="", font=("Arial", 50), bg_color='white', text_color="black")
display.pack(pady=100, padx=15, anchor='e')

def definir_operacao(op):
    global valor_anterior, valor_atual, operacao
    valor_anterior = valor_atual
    operacao = op
    valor_atual = "" 

def formatar_numero(numero):
    partes = f"{float(numero):,.0f}".split(',')
    return '.'.join(partes)

def calcular_resultado():
    global valor_atual, valor_anterior, operacao
    try:
        if operacao == "+":
            resultado = float(valor_anterior) + float(valor_atual)
        elif operacao == "-":
            resultado = float(valor_anterior) - float(valor_atual)
        elif operacao == "x":
            resultado = float(valor_anterior) * float(valor_atual)
        elif operacao == "%":
            resultado = float(valor_anterior) % float(valor_atual)
        elif operacao == "÷":
            if float(valor_atual) != 0:
                resultado = float(valor_anterior) / float(valor_atual)
            else:
                display.configure(text="Burro")
                return
        else:
            resultado = float(valor_atual)

        resultado_formatado = formatar_numero(str(resultado))
        display.configure(text=resultado_formatado) 
        valor_atual = str(resultado) 
        operacao = "" 
    except ValueError:
        display.configure(text="Erro") 

def alternar_sinal():
    global valor_atual
    if valor_atual:
        if valor_atual.startswith('-'):
            valor_atual = valor_atual[1:]
        else:
            valor_atual = '-' + valor_atual
        display.configure(text=valor_atual)

def apagarnum():
    global valor_atual
    if valor_atual:
        valor_atual = valor_atual[:-1]
        display.configure(text=valor_atual)

def apagartudo():
    global valor_atual, valor_anterior, operacao
    valor_atual = ""
    valor_anterior = ""
    operacao = ""
    display.configure(text="")

def apagarentrada():
    global valor_atual
    valor_atual = ""
    display.configure(text="") 

def virgulaa():
    global valor_atual
    if '.' not in valor_atual:
        if valor_atual == "":
            valor_atual = "0."
        else:
            valor_atual += "."
        display.configure(text=valor_atual)

def calcular_inverso():
    global valor_atual
    try:
        valor_atual = str(1 / float(valor_atual))
        display.configure(text=valor_atual)
    except ZeroDivisionError:
        display.configure(text="Erro")
    except ValueError:
        display.configure(text="Erro")

def calcular_quadrado():
    global valor_atual
    try:
        valor_atual = str(float(valor_atual) ** 2)
        display.configure(text=valor_atual)
    except ValueError:
        display.configure(text="Erro")

def calcular_raiz_quadrada():
    global valor_atual
    try:
        valor_atual = str(float(valor_atual) ** 0.5)
        display.configure(text=valor_atual)
    except ValueError:
        display.configure(text="Erro")

def open_video():
    video_path = "muehehehe.mp4"
    if os.name == 'nt':  # Windows
        os.startfile(video_path)

muehehehe = ctk.CTkButton(app, height=20, width=40, text='MUEHEHEHE', fg_color='hotpink', corner_radius=0, command=open_video)
muehehehe.place(x=5, y=5)

mc = ctk.CTkButton(app, height=20, width=40, text='MC', fg_color='hotpink', corner_radius=0)
mc.place(x=5, y=175)

mr = ctk.CTkButton(app, height=20, width=40, text='MR', fg_color='hotpink', corner_radius=0)
mr.place(x=60, y=175)

mmais = ctk.CTkButton(app, height=20, width=40, text='M+', fg_color='hotpink', corner_radius=0)
mmais.place(x=115, y=175)

mmenos = ctk.CTkButton(app, height=20, width=40, text='M-', fg_color='hotpink', corner_radius=0)
mmenos.place(x=165, y=175)

ms = ctk.CTkButton(app, height=20, width=40, text='MS', fg_color='hotpink', corner_radius=0)
ms.place(x=220, y=175)

mv = ctk.CTkButton(app, height=20, width=40, text='Mv', fg_color='hotpink', corner_radius=0)
mv.place(x=275, y=175)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=5, y=202)

porcentagem = ctk.CTkButton(app, height=50, width=70, text='%', fg_color='dimgray', corner_radius=0, command=lambda: definir_operacao('%'))
porcentagem.place(x=5, y=200)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=245, y=202)

apagar = ctk.CTkButton(app, height=50, width=70, text='←', fg_color='dimgray', corner_radius=0, command=apagarnum)
apagar.place(x=245, y=200)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=85, y=202)

ce = ctk.CTkButton(app, height=50, width=70, text='CE', fg_color='dimgray', corner_radius=0, command=apagarentrada)
ce.place(x=85, y=200)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=165, y=202)

c = ctk.CTkButton(app, height=50, width=70, text='C', fg_color='dimgray', corner_radius=0, command=apagartudo)
c.place(x=165, y=200)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=5, y=257)

umbarrax = ctk.CTkButton(app, height=50, width=70, text='1/x', fg_color='dimgray', corner_radius=0, command=calcular_inverso)
umbarrax.place(x=5, y=255)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=85, y=257)

xdois = ctk.CTkButton(app, height=50, width=70, text='x²', fg_color='dimgray', corner_radius=0, command=calcular_quadrado)
xdois.place(x=85, y=255)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=165, y=257)

doisvx = ctk.CTkButton(app, height=50, width=70, text='²√x', fg_color='dimgray', corner_radius=0, command=calcular_raiz_quadrada)
doisvx.place(x=165, y=255)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=245, y=257)

dividir = ctk.CTkButton(app, height=50, width=70, text='÷', fg_color='dimgray', corner_radius=0, command=lambda: definir_operacao('÷'))
dividir.place(x=245, y=255)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=5, y=312)

sete = ctk.CTkButton(app, height=50, width=70, text='7', fg_color='gray', corner_radius=0, command=lambda: exibir_numero(7))
sete.place(x=5, y=310)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=85, y=312)

oito = ctk.CTkButton(app, height=50, width=70, text='8', fg_color='gray', corner_radius=0, command=lambda: exibir_numero(8))
oito.place(x=85, y=310)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=165, y=312)

nove = ctk.CTkButton(app, height=50, width=70, text='9', fg_color='gray', corner_radius=0, command=lambda: exibir_numero(9))
nove.place(x=165, y=310)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=245, y=312)

multiplicar = ctk.CTkButton(app, height=50, width=70, text='x', fg_color='dimgray', corner_radius=0, command=lambda: definir_operacao('x'))
multiplicar.place(x=245, y=310)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=5, y=367)

quatro = ctk.CTkButton(app, height=50, width=70, text='4', fg_color='gray', corner_radius=0, command=lambda: exibir_numero(4))
quatro.place(x=5, y=365)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=85, y=367)

cinco = ctk.CTkButton(app, height=50, width=70, text='5', fg_color='gray', corner_radius=0, command=lambda: exibir_numero(5))
cinco.place(x=85, y=365)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=165, y=367)

seis = ctk.CTkButton(app, height=50, width=70, text='6', fg_color='gray', corner_radius=0, command=lambda: exibir_numero(6))
seis.place(x=165, y=365)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=245, y=367)

subtrair = ctk.CTkButton(app, height=50, width=70, text='-', fg_color='dimgray', corner_radius=0, command=lambda: definir_operacao('-'))
subtrair.place(x=245, y=365)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=5, y=422)

um = ctk.CTkButton(app, height=50, width=70, text='1', fg_color='gray', corner_radius=0, command=lambda: exibir_numero(1))
um.place(x=5, y=420)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=85, y=422)

dois = ctk.CTkButton(app, height=50, width=70, text='2', fg_color='gray', corner_radius=0, command=lambda: exibir_numero(2))
dois.place(x=85, y=420)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=165, y=422)

tres = ctk.CTkButton(app, height=50, width=70, text='3', fg_color='gray', corner_radius=0, command=lambda: exibir_numero(3))
tres.place(x=165, y=420)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=245, y=422)

somar = ctk.CTkButton(app, height=50, width=70, text='+', fg_color='dimgray', corner_radius=0, command=lambda: definir_operacao('+'))
somar.place(x=245, y=420)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=5, y=477)

maismenos = ctk.CTkButton(app, height=50, width=70, text='+/-', fg_color='gray', corner_radius=0, command=alternar_sinal)
maismenos.place(x=5, y=475)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=85, y=477)

zero = ctk.CTkButton(app, height=50, width=70, text='0', fg_color='gray', corner_radius=0, command=lambda: exibir_numero(0))
zero.place(x=85, y=475)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=165, y=477)

virgula = ctk.CTkButton(app, height=50, width=70, text=',', fg_color='gray', corner_radius=0, command=virgulaa)
virgula.place(x=165, y=475)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=245, y=477)

igual = ctk.CTkButton(app, height=50, width=70, text='=', fg_color='hotpink', corner_radius=0, command=calcular_resultado)
igual.place(x=245, y=475)

app.mainloop()
 