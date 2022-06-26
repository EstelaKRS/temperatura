#PREGUNTA1
import calendar as c
import datetime
import numpy as np
import pandas as pd
#PARA SUMAR la lista
def suma(l,n):
    s=[]
    for i in range(0,n):
        s.append(l[i])
    return sum(s)
#PARA LA PREGUNTA 1
def tiempo(año):
    if(c.isleap(año)):
        print("El año es biciesto")
        month=[31,29,31,30,31,30,31,31,30,31,30,31]
        dia=int(input("Ingresar la fecha:"))
        mes=input(("Ingrese mes:"))
        print("Fecha a pedir",(dia,mes))
        if(mes=="ENERO" and 0<dia<=31):
            d=dia
            return print(d)
        elif(mes=="FEBRERO" and 0<dia<=29):
            d=dia+suma(month,1)
            return print(d)
        elif(mes=="MARZO" and 0<dia<=31):
            d=dia+suma(month,2)
            return print(d)
        elif(mes=="ABRIL" and 0<dia<=30):
            d=dia+suma(month,3)
            return print(d)
        elif(mes=="MAYO" and 0<dia<=31):
            d=dia+suma(month,4)
            return print(d)
        elif(mes=="JUNIO" and 0<dia<=30):
            d=dia+suma(month,5)
            return print(d)
        elif(mes=="JULIO" and 0<dia<=31):
            d=dia+suma(month,6)
            return print(d)
        elif(mes=="AGOSTO" and 0<dia<= 31):
            d=dia+suma(month,7)
            return print(d)
        elif(mes=="SETIEMBRE" and 0<dia<=30):
            d=dia+suma(month,8)
            return print(d)
        elif(mes=="Octubre" and 0<dia<=31):
            d=dia+suma(month,9)
            return print(d)
        elif(mes=="Noviembre" and 0<dia<= 30):
            d=dia+suma(month,10)
            return print(d)
        elif(mes=="Diciembre" and 0<dia<= 31):
            d=dia+suma(month,11)
            return print(d)
    else:
        print("El año no es bisiesto")
        m=[31,28,31,30,31,30,31,31,30,31,30,31]
        dia=int(input("ingrese fecha:"))
        mes=input("ingrese mes:")
        print("Fecha a pedir",(dia,mes))
        if (mes=="Enero" and 0<dia<=31):
            d=dia
            return print(d)
        elif(mes=="Febrero" and 0<dia<=28):
            d=dia+suma(m,1)
            return print(d)
        elif(mes=="Marzo" and 0<dia<=31):
            d=dia+suma(m,2)
            return print(d)
        elif(mes=="Abril" and 0<dia<=30):
            d=dia+suma(m,3)
            return print(d)
        elif(mes=="Mayo" and 0<dia<=31):
            d=dia+suma(m,4)
            return print(d)
        elif(mes=="Junio" and 0<dia<=30):
            d=dia+suma(m,5)
            return print(d)
        elif(mes=="Julio" and 0<dia<=31):
            d=dia+suma(m,6)
            return print(d)
        elif(mes=="Agosto" and 0<dia<=31):
            d=dia+suma(m,7)
            return print(d)
        elif(mes=="Setiembre" and 0<dia<=30):
            d=dia+suma(m,8)
            return print(d)
        elif(mes=="Octubre" and 0<dia<=31):
            d=dia+suma(m,9)
            return print(d)
        elif(mes=="Noviembre" and 0<dia<=30):
            d=dia+suma(m,10)
            return print(d)
        elif(mes=="Diciembre" and 0<dia<=31):
            d=dia+suma(m,11)
            return print(d)

tiempo(1997)
