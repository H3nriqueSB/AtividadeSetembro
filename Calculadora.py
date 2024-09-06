import customtkinter as ctk
from PIL import Image, ImageTk
import os

app = ctk.CTk()
app.geometry('320x530')
app.configure(fg_color='black')
app.title('Caladoraneitor')

def atualizar_texto(texto):
    texto_label.config(text=texto)

texto_label = ctk.CTkLabel(app, text="", font=("Arial", 24))
texto_label.place(x=100, y=100)

img_path = 'bg.png'
img = Image.open(img_path) 
background = ImageTk.PhotoImage(img)

label_img = ctk.CTkLabel(app, image=background, text='')
label_img.place(x=0, y=0)

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

porcentagem = ctk.CTkButton(app, height=50, width=70, text='%', fg_color='dimgray', corner_radius=0)
porcentagem.place(x=5, y=200)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=245, y=202)

apagar = ctk.CTkButton(app, height=50, width=70, text='<x]', fg_color='dimgray', corner_radius=0)
apagar.place(x=245, y=200)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=85, y=202)

ce = ctk.CTkButton(app, height=50, width=70, text='CE', fg_color='dimgray', corner_radius=0)
ce.place(x=85, y=200)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=165, y=202)

c = ctk.CTkButton(app, height=50, width=70, text='C', fg_color='dimgray', corner_radius=0)
c.place(x=165, y=200)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=5, y=257)

umbarrax = ctk.CTkButton(app, height=50, width=70, text='1/x', fg_color='dimgray', corner_radius=0)
umbarrax.place(x=5, y=255)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=85, y=257)

xdois = ctk.CTkButton(app, height=50, width=70, text='x²', fg_color='dimgray', corner_radius=0)
xdois.place(x=85, y=255)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=165, y=257)

doisvx = ctk.CTkButton(app, height=50, width=70, text='²√x', fg_color='dimgray', corner_radius=0)
doisvx.place(x=165, y=255)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=245, y=257)

dividir = ctk.CTkButton(app, height=50, width=70, text='÷', fg_color='dimgray', corner_radius=0)
dividir.place(x=245, y=255)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=5, y=312)

sete = ctk.CTkButton(app, height=50, width=70, text='7', fg_color='gray', corner_radius=0, command=lambda: atualizar_texto("7"))
sete.place(x=5, y=310)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=85, y=312)

oito = ctk.CTkButton(app, height=50, width=70, text='8', fg_color='gray', corner_radius=0)
oito.place(x=85, y=310)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=165, y=312)

nove = ctk.CTkButton(app, height=50, width=70, text='9', fg_color='gray', corner_radius=0)
nove.place(x=165, y=310)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=245, y=312)

multiplicar = ctk.CTkButton(app, height=50, width=70, text='x', fg_color='dimgray', corner_radius=0)
multiplicar.place(x=245, y=310)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=5, y=367)

quatro = ctk.CTkButton(app, height=50, width=70, text='4', fg_color='gray', corner_radius=0)
quatro.place(x=5, y=365)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=85, y=367)

cinco = ctk.CTkButton(app, height=50, width=70, text='5', fg_color='gray', corner_radius=0)
cinco.place(x=85, y=365)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=165, y=367)

seis = ctk.CTkButton(app, height=50, width=70, text='6', fg_color='gray', corner_radius=0)
seis.place(x=165, y=365)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=245, y=367)

subtrair = ctk.CTkButton(app, height=50, width=70, text='-', fg_color='dimgray', corner_radius=0)
subtrair.place(x=245, y=365)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=5, y=422)

um = ctk.CTkButton(app, height=50, width=70, text='1', fg_color='gray', corner_radius=0)
um.place(x=5, y=420)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=85, y=422)

dois = ctk.CTkButton(app, height=50, width=70, text='2', fg_color='gray', corner_radius=0)
dois.place(x=85, y=420)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=165, y=422)

tres = ctk.CTkButton(app, height=50, width=70, text='3', fg_color='gray', corner_radius=0)
tres.place(x=165, y=420)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=245, y=422)

somar = ctk.CTkButton(app, height=50, width=70, text='+', fg_color='dimgray', corner_radius=0)
somar.place(x=245, y=420)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=5, y=477)

maismenos = ctk.CTkButton(app, height=50, width=70, text='+/-', fg_color='gray', corner_radius=0)
maismenos.place(x=5, y=475)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=85, y=477)

zero = ctk.CTkButton(app, height=50, width=70, text='0', fg_color='gray', corner_radius=0)
zero.place(x=85, y=475)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=165, y=477)

virgula = ctk.CTkButton(app, height=50, width=70, text=',', fg_color='gray', corner_radius=0)
virgula.place(x=165, y=475)

fundbutt = ctk.CTkFrame(app, height=50, width=70, fg_color='black')
fundbutt.place(x=245, y=477)

igual = ctk.CTkButton(app, height=50, width=70, text='=', fg_color='hotpink', corner_radius=0)
igual.place(x=245, y=475)

app.mainloop()
 