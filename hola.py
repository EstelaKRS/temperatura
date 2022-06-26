from tkinter import *
from PIL import Image, ImageTk
temps = ["Celsius", " Fahrenheit","Kelvin","Rankine"]#variable
OPTIONS = ["selec unidades",
           "Celsius",
           "Fahrenheit",
           "Kelvin",
           "Rankine"]
raiz=Tk()
raiz.title("Conversión Estela-Metereología")
raiz.resizable(True,False) #parametro ancho alto
raiz.iconbitmap("C:/Users/Estelamaris/Documents/metereologia/escudo.ico")
#raiz.geometry("620x350")
raiz.config(bg = "gray") #gray

titulo_label=Label(raiz,text="Conversión de Escalas de Temperatura",anchor=CENTER, fg="light blue",bg="gray")
titulo_label.config(font=("Comic Sans MS",20))
titulo_label.grid(row=0,column=0,columnspan=10, pady=5)

img = Image.open("C:/Users/Estelamaris/Documents/metereologia/Captura4.PNG")
img = img.resize((50,100))
img = ImageTk.PhotoImage(img)
img_lbl = Label(raiz, image=img, bg="gray")
img_lbl.image = img
img_lbl.grid(row=3, column=5, columnspan=4, padx=5, pady=5)

def convertir():
        ent = float(inputentry.get()) #entry
        ent_unit = inputopt.get()
        out_unit = outputopt.get()

        cons = [ent_unit in temps and out_unit in temps]

        if any(cons):  # si escogemos cualquiera de las mismas unidades
            if ent_unit == "Celsius" and out_unit == "Celsius":
                outputentry.delete(0, END)  # borrado automatico
                outputentry.insert(0, (ent * 1))
            elif ent_unit == "Celsius" and out_unit == "Fahrenheit":
                outputentry.delete(0, END)
                outputentry.insert(0, (ent * 1.8) + 32)
            elif ent_unit == "Celsius" and out_unit == "Kelvin":
                outputentry.delete(0, END)
                outputentry.insert(0, (ent + 273))
            elif ent_unit == "Celsius" and out_unit == "Rankine":
                outputentry.delete(0, END)
                outputentry.insert(0, (ent * 1.8) + 491.67)
            elif ent_unit == "Fahrenheit" and out_unit == "Celsius":
                outputentry.delete(0, END)
                outputentry.insert(0, (ent - 32) * (5 / 9))
            elif ent_unit == "Fahrenheit" and out_unit == "Fahrenheit":
                outputentry.delete(0, END)
                outputentry.insert(0, (ent * 1))
            elif ent_unit == "Fahrenheit" and out_unit == "Kelvin":
                outputentry.delete(0, END)
                outputentry.insert(0, (ent - 32) * (5 / 9) + 273.15)
            elif ent_unit == "Fahrenheit" and out_unit == "Rankine":
                outputentry.delete(0, END)
                outputentry.insert(0, (ent * 1) + 259.67)
            elif ent_unit == "Kelvin" and out_unit == "Celsius":
                outputentry.delete(0, END)
                outputentry.insert(0, (ent + 273))
            elif ent_unit == "Kelvin" and out_unit == "Fahrenheit":
                outputentry.delete(0, END)
                outputentry.insert(0, (ent - 273) * 1.8 + 32)
            elif ent_unit == "Kelvin" and out_unit == "Kelvin":
                outputentry.delete(0, END)
                outputentry.insert(0, (ent * 1))
            elif ent_unit == "Kelvin" and out_unit == "Rankine":
                outputentry.delete(0, END)
                outputentry.insert(0, (ent * 1.8))
            elif ent_unit == "Rankine" and out_unit == "Celsius":
                outputentry.delete(0, END)
                outputentry.insert(0, (ent - 491.67) * (5 / 9))
            elif ent_unit == "Rankine" and out_unit == "Fahrenheit":
                outputentry.delete(0, END)
                outputentry.insert(0, (ent - 491.67))
            elif ent_unit == "Rankine" and out_unit == "Kelvin":
                outputentry.delete(0, END)
                outputentry.insert(0, ent * (5 / 9))
            elif ent_unit == "Rankine" and out_unit == "Rankine":
                outputentry.delete(0, END)
                outputentry.insert(0, (ent * 1))
            else:
                outputentry.delete(0, END)

        else:  # muestra error si las unidades son del mismo tipo
            outputentry.delete(0, END)
            outputentry.insert(0, "ERROR")

inputopt = StringVar()
inputopt.set(OPTIONS[0])

outputopt = StringVar()
outputopt.set(OPTIONS[0])


inputlabel = Label(raiz, text="Cantidad :")
inputlabel.config(fg="light blue", bg="gray")
inputlabel.grid(row=1, column=0, padx=5, pady=5)
inputlabel.config(font=("Comic Sans MS",15))

inputentry = Entry(raiz)
inputentry.grid(row=1, column=1, padx=5, pady=5)
inputentry.config(justify="center")

inputmenu = OptionMenu(raiz, inputopt, *OPTIONS) #seleccion de unidades
inputmenu.grid(row=1, column=5)
inputmenu.config(font="Times 10")

outputlabel = Label(raiz, text="Resultado:", font="Times")
outputlabel.config(fg="light blue", bg="gray")
outputlabel.config(font=("Comic Sans Ms",15))
outputlabel.grid(row=2, column=0, padx=5, ipady=5)

outputentry = Entry(raiz, font="Times")
outputentry.grid(row=2, column=1, padx=5, pady=5)
outputentry.config(justify="center")
outputmenu = OptionMenu(raiz, outputopt, *OPTIONS)
outputmenu.grid(row=2, column=5)
outputmenu.config(font="Times 10")

cbtn = Button(raiz, text="convertir", command=convertir, padx=80, pady=2)
cbtn.grid(row=3, column=0, columnspan=2, pady=50)
cbtn.config(font=("Comic Sans MS",10))

raiz.mainloop()