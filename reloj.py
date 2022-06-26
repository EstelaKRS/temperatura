from tkinter import *
from PIL import Image, ImageTk
import calendar as c

#temps = ["Enero"," Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto",
        # "Setiembre","Octubre","Noviembre","Diciembre"]#variable
OPTIONS = ["Enero","Febreo","Marzo","Abril","Mayo","Junio","Julio","Agosto",
           "Setiembre","Octubre","Noviembre","Diciembre"]
raiz=Tk()
raiz.title("Conversión Estela-Metereologia")
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

def suma(l,n):
    s=[]
    for i in range(0,n):
        s.append(l[i])
        return sum(s)
def convertir():
        ent = float(inputentry.get()) #entry, año
        ent_unit = float(inputentry1.get()) #dia
        ent_unit1 = inputopt.get() #mes

        if c.isleap(ent):
            ms=[31,29,31,30,31,30,31,31,30,31,30,31]
            if ent_unit1 == "Enero" and 0<ent_unit<=31:
                outputentry.delete(0, END)
                outputentry.insert(0,(ent_unit))
                et.delete(0, END)
                et.insert(0, "BISIESTO")
            elif ent_unit1 == "Febrero" and 0<ent_unit<=29:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit+suma(ms,1)))
                et.delete(0, END)
                et.insert(0, "BISIESTO")
            elif ent_unit1 == "Marzo" and 0<ent_unit<=31:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit+suma(ms,2)))
                et.delete(0, END)
                et.insert(0, "BISIESTO")
            elif ent_unit1 == "Abril" and 0<ent_unit<=30:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit+suma(ms,3)))
                et.delete(0,END)
                et.insert(0, "BISIESTO")
            elif ent_unit1 == "Mayo" and 0<ent_unit<=31:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit+suma(ms,4)))
                et.delete(0, END)
                et.insert(0, "BISIESTO")
            elif ent_unit1 == "Junio" and 0<ent_unit<=30:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit+suma(ms,5)))
                et.delete(0, END)
                et.insert(0, "BISIESTO")
            elif ent_unit1 == "Julio" and 0<ent_unit<=31:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit+suma(ms,6)))
                et.delete(0, END)
                et.insert(0, "BISIESTO")
            elif ent_unit1 == "Agosto" and 0<ent_unit<=31:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit+suma(ms,7)))
                et.delete(0, END)
                et.insert(0, "BISIESTO")
            elif ent_unit1 == "Setiembre" and 0<ent_unit<=30:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit+suma(ms,8)))
                et.delete(0, END)
                et.insert(0, "BISIESTO")
            elif ent_unit1 == "Octubre" and 0<ent_unit<=31:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit+suma(ms,9)))
                et.delete(0, END)
                et.insert(0, "BISIESTO")
            elif ent_unit1 == "Noviembre" and 0<ent_unit<=30:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit+suma(ms,10)))
                et.delete(0, END)
                et.insert(0, "BISIESTO")
            elif ent_unit1 == "Diciembre" and 0<ent_unit<=31:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit+suma(ms,11)))
                et.delete(0, END)
                et.insert(0, "BISIESTO")
        else:
            ms=[31,28,31,30,31,30,31,31,30,31,30,31]
            if ent_unit1 == "Enero" and 0<ent_unit<=31:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit))
                et.delete(0, END)
                et.insert(0, "NO BISIESTO")
            elif ent_unit1 == "Febrero" and 0<ent_unit<=28:
                outputentry.delete(0, END)
                outputentry.insert(0,(ent_unit+suma(ms,1)))
                et.delete(0, END)
                et.insert(0, "NO BISIESTO")
            elif ent_unit1 == "Marzo" and 0<ent_unit<=31:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit+suma(ms,2)))
                et.delete(0, END)
                et.insert(0, "NO BISIESTO")
            elif ent_unit1 == "Abril" and 0<ent_unit<=30:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit+suma(ms,3)))
                et.delete(0, END)
                et.insert(0, "NO BISIESTO")
            elif ent_unit1 == "Mayo" and 0<ent_unit<=31:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit+suma(ms,4)))
                et.delete(0, END)
                et.insert(0, "NO BISIESTO")
            elif ent_unit1 == "Junio" and 0<ent_unit<=30:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit+suma(ms,5)))
                et.delete(0, END)
                et.insert(0, "NO BISIESTO")
            elif ent_unit1 == "Julio" and 0<ent_unit<=31:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit+suma(ms,6)))
                et.delete(0, END)
                et.insert(0, "NO BISIESTO")
            elif ent_unit1 == "Agosto" and 0<ent_unit<=31:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit+suma(ms,7)))
                et.delete(0, END)
                et.insert(0, "NO BISIESTO")
            elif ent_unit1 == "Setiembre" and 0<ent_unit<=30:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit+suma(ms,8)))
                et.delete(0, END)
                et.insert(0, "NO BISIESTO")
            elif ent_unit1 == "Octubre" and 0<ent_unit<=31:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit+suma(ms,9)))
                et.delete(0, END)
                et.insert(0, "NO BISIESTO")
            elif ent_unit1 == "Noviembre" and 0<ent_unit<=30:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit+suma(ms,10)))
                et.delete(0, END)
                et.insert(0, "NO BISIESTO")
            elif ent_unit1 == "Diciembre" and 0<ent_unit<=31:
                outputentry.delete(0, END)
                outputentry.insert(0, (ent_unit+suma(ms,11)))
                et.delete(0, END)
                et.insert(0, "NO BISIESTO")



inputopt = StringVar()
inputopt.set(OPTIONS[0])

#outputopt = StringVar()
#outputopt.set(OPTIONS[0])


inputlabel = Label(raiz, text="Mes :")
inputlabel.config(fg="light blue", bg="gray")
inputlabel.grid(row=1, column=2, padx=10, pady=10)
inputlabel.config(font=("Comic Sans MS",15))

inputlabel = Label(raiz, text="Año :")
inputlabel.config(fg="light blue", bg="gray")
inputlabel.grid(row=1, column=0, padx=5, pady=5)
inputlabel.config(font=("Comic Sans MS",15))

inputentry = Entry(raiz)
inputentry.grid(row=1, column=1, padx=5, pady=5)
inputentry.config(justify="center")

inputENTRADA = Label(raiz, text="tipo :")
inputENTRADA.config(fg="light blue", bg="gray")
inputENTRADA.grid(row=2, column=0, padx=5, pady=5)
inputENTRADA.config(font=("Comic Sans MS",15))

et = Entry(raiz)
et.grid(row=2, column=1, padx=5, pady=5)
et.config(justify="center")

inputddd = Label(raiz, text="día :")
inputddd.config(fg="light blue", bg="gray")
inputddd.grid(row=3, column=0, padx=5, pady=5)
inputddd.config(font=("Comic Sans MS",15))

inputentry1 = Entry(raiz)
inputentry1.grid(row=3, column=1, padx=5, pady=5)
inputentry1.config(justify="center")

inputmenu = OptionMenu(raiz, inputopt, *OPTIONS) #seleccion de unidades
inputmenu.grid(row=1, column=5)
inputmenu.config(font="Times 10")

outputlabel = Label(raiz, text="Resultado:")
outputlabel.config(fg="light blue", bg="gray")
outputlabel.config(font=("Comic Sans Ms",15))
outputlabel.grid(row=4, column=0, padx=5, ipady=5)

outputentry = Entry(raiz, font="Times")
outputentry.grid(row=4, column=1, padx=5, pady=5)
outputentry.config(justify="center")

#outputmenu = OptionMenu(raiz, outputopt, *OPTIONS)
#outputmenu.grid(row=2, column=5)
#outputmenu.config(font="Times 10")

cbtn = Button(raiz, text="convertir", command=convertir, padx=80, pady=2)
cbtn.grid(row=5, column=0, columnspan=2, pady=50)
cbtn.config(font=("Comic Sans MS",10))

raiz.mainloop()