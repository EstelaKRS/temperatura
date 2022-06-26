import pandas as pd
import operator
def diference(x):
  c=['weatherdata-311-922.csv','weatherdata-695-1294.csv','weatherdata-7571000.csv',
     'weatherdata--8-803.csv','weatherdata--117-778.csv','weatherdata--301-513.csv',
     'weatherdata--548-684.csv']
  if(x==1):
   datos5=pd.read_csv(c[0],index_col=False)
   col=['Date','Max Temperature','Min Temperature']
   temp5=pd.DataFrame(datos5,columns=col)
   #p2=temp.assign(Tmax_Tmin=temp['Max Temperature']-temp['Min Temperature'])
   p2=(temp5['Max Temperature']-temp5['Min Temperature']).abs()
   p3=temp5.assign(Tmax_Tmin=p2)#resultado para 1 estacion meteorologica
   colw=['Date','Tmax_Tmin']
   tempw=pd.DataFrame(p3,columns=colw)
   dw=dict(zip(tempw['Date'],tempw['Tmax_Tmin']))
   maxf_key = max(dw, key = dw.get)
   valorw=dw.get(maxf_key)
   print('La fecha de max amplitud termica es:',maxf_key,valorw)
  if(x==2):
   datos5=pd.read_csv(c[1],index_col=False)
   col=['Date','Max Temperature','Min Temperature']
   temp5=pd.DataFrame(datos5,columns=col)
   #p2=temp.assign(Tmax_Tmin=temp['Max Temperature']-temp['Min Temperature'])
   p2=(temp5['Max Temperature']-temp5['Min Temperature']).abs()
   p3=temp5.assign(Tmax_Tmin=p2)#resultado para 1 estacion meteorologica
   colw=['Date','Tmax_Tmin']
   tempw=pd.DataFrame(p3,columns=colw)
   dw=dict(zip(tempw['Date'],tempw['Tmax_Tmin']))
   maxf_key = max(dw, key = dw.get)
   valorw=dw.get(maxf_key)
   print('La fecha de max amplitud termica es:',maxf_key,valorw)
  if(x==3):
   datos5=pd.read_csv(c[2],index_col=False)
   col=['Date','Max Temperature','Min Temperature']
   temp5=pd.DataFrame(datos5,columns=col)
   #p2=temp.assign(Tmax_Tmin=temp['Max Temperature']-temp['Min Temperature'])
   p2=(temp5['Max Temperature']-temp5['Min Temperature']).abs()
   p3=temp5.assign(Tmax_Tmin=p2)#resultado para 1 estacion meteorologica
   colw=['Date','Tmax_Tmin']
   tempw=pd.DataFrame(p3,columns=colw)
   dw=dict(zip(tempw['Date'],tempw['Tmax_Tmin']))
   maxf_key = max(dw, key = dw.get)
   valorw=dw.get(maxf_key)
   print('La fecha de max amplitud termica es:',maxf_key,valorw)
  if(x==4):
   datos5=pd.read_csv(c[3],index_col=False)
   col=['Date','Max Temperature','Min Temperature']
   temp5=pd.DataFrame(datos5,columns=col)
   #p2=temp.assign(Tmax_Tmin=temp['Max Temperature']-temp['Min Temperature'])
   p2=(temp5['Max Temperature']-temp5['Min Temperature']).abs()
   p3=temp5.assign(Tmax_Tmin=p2)#resultado para 1 estacion meteorologica
   colw=['Date','Tmax_Tmin']
   tempw=pd.DataFrame(p3,columns=colw)
   dw=dict(zip(tempw['Date'],tempw['Tmax_Tmin']))
   maxf_key = max(dw, key = dw.get)
   valorw=dw.get(maxf_key)
   print('La fecha de max amplitud termica es:',maxf_key,valorw)
  if(x==5):
   datos5=pd.read_csv(c[4],index_col=False)
   col=['Date','Max Temperature','Min Temperature']
   temp5=pd.DataFrame(datos5,columns=col)
   #p2=temp.assign(Tmax_Tmin=temp['Max Temperature']-temp['Min Temperature'])
   p2=(temp5['Max Temperature']-temp5['Min Temperature']).abs()
   p3=temp5.assign(Tmax_Tmin=p2)#resultado para 1 estacion meteorologica
   colw=['Date','Tmax_Tmin']
   tempw=pd.DataFrame(p3,columns=colw)
   dw=dict(zip(tempw['Date'],tempw['Tmax_Tmin']))
   maxf_key = max(dw, key = dw.get)
   valorw=dw.get(maxf_key)
   print('La fecha de max amplitud termica es:',maxf_key,valorw)
  if(x==6):
   datos5=pd.read_csv(c[5],index_col=False)
   col=['Date','Max Temperature','Min Temperature']
   temp5=pd.DataFrame(datos5,columns=col)
   #p2=temp.assign(Tmax_Tmin=temp['Max Temperature']-temp['Min Temperature'])
   p2=(temp5['Max Temperature']-temp5['Min Temperature']).abs()
   p3=temp5.assign(Tmax_Tmin=p2)#resultado para 1 estacion meteorologica
   colw=['Date','Tmax_Tmin']
   tempw=pd.DataFrame(p3,columns=colw)
   dw=dict(zip(tempw['Date'],tempw['Tmax_Tmin']))
   maxf_key = max(dw, key = dw.get)
   valorw=dw.get(maxf_key)
   print('La fecha de max amplitud termica es:',maxf_key,valorw)
  if(x==7):
   datos5=pd.read_csv(c[6],index_col=False)
   col=['Date','Max Temperature','Min Temperature']
   temp5=pd.DataFrame(datos5,columns=col)
   #p2=temp.assign(Tmax_Tmin=temp['Max Temperature']-temp['Min Temperature'])
   p2=(temp5['Max Temperature']-temp5['Min Temperature']).abs()
   p3=temp5.assign(Tmax_Tmin=p2)#resultado para 1 estacion meteorologica
   colw=['Date','Tmax_Tmin']
   tempw=pd.DataFrame(p3,columns=colw)
   dw=dict(zip(tempw['Date'],tempw['Tmax_Tmin']))
   maxf_key = max(dw, key = dw.get)
   valorw=dw.get(maxf_key)
   print('La fecha de max amplitud termica es:',maxf_key,valorw)

def TM(x):
  c=['weatherdata--117-778.csv','weatherdata--301-513.csv','weatherdata--548-684.csv',
     'weatherdata--8-803.csv','weatherdata-311-922.csv','weatherdata-695-1294.csv',
     'weatherdata-7571000.csv']
  if(x==1):
    data=pd.read_csv(c[0],index_col=False)
    colx=['Date','Max Temperature']
    coly=['Date','Min Temperature']
    tempx=pd.DataFrame(data,columns=colx)
    tempy=pd.DataFrame(data,columns=coly)
    d=dict(zip(tempx['Date'],tempx['Max Temperature']))
    d1=dict(zip(tempy['Date'],tempy['Min Temperature']))
    max_key = max(d, key = d.get)
    min_key=min(d1,key=d1.get)
    valor1=d.get(max_key)
    valor2=d1.get(min_key)
    print('La fecha de max temperatura es:',max_key,valor1)
    print('La fecha de min temperatura es:',min_key,valor2)
    diference(1)
  elif(x==2):
    data=pd.read_csv(c[1],index_col=False)
    colx=['Date','Max Temperature']
    coly=['Date','Min Temperature']
    tempx=pd.DataFrame(data,columns=colx)
    tempy=pd.DataFrame(data,columns=coly)
    d=dict(zip(tempx['Date'],tempx['Max Temperature']))
    d1=dict(zip(tempy['Date'],tempy['Min Temperature']))
    max_key = max(d, key = d.get)
    min_key=min(d1,key=d1.get)
    valor1=d.get(max_key)
    valor2=d1.get(min_key)
    print('La fecha de max temperatura es:',max_key,valor1)
    print('La fecha de min temperatura es:',min_key,valor2)
    diference(2)

  elif(x==3):
    data=pd.read_csv(c[2],index_col=False)
    colx=['Date','Max Temperature']
    coly=['Date','Min Temperature']
    tempx=pd.DataFrame(data,columns=colx)
    tempy=pd.DataFrame(data,columns=coly)
    d=dict(zip(tempx['Date'],tempx['Max Temperature']))
    d1=dict(zip(tempy['Date'],tempy['Min Temperature']))
    max_key = max(d, key = d.get)
    min_key=min(d1,key=d1.get)
    valor1=d.get(max_key)
    valor2=d1.get(min_key)
    print('La fecha de max temperatura es:',max_key,valor1)
    print('La fecha de min temperatura es:',min_key,valor2)
    diference(3)

  elif(x==4):
    data=pd.read_csv(c[3],index_col=False)
    colx=['Date','Max Temperature']
    coly=['Date','Min Temperature']
    tempx=pd.DataFrame(data,columns=colx)
    tempy=pd.DataFrame(data,columns=coly)
    d=dict(zip(tempx['Date'],tempx['Max Temperature']))
    d1=dict(zip(tempy['Date'],tempy['Min Temperature']))
    max_key = max(d, key = d.get)
    min_key=min(d1,key=d1.get)
    valor1=d.get(max_key)
    valor2=d1.get(min_key)
    print('La fecha de max temperatura es:',max_key,valor1)
    print('La fecha de min temperatura es:',min_key,valor2)
    diference(4)

  elif(x==5):
    data=pd.read_csv(c[4],index_col=False)
    colx=['Date','Max Temperature']
    coly=['Date','Min Temperature']
    tempx=pd.DataFrame(data,columns=colx)
    tempy=pd.DataFrame(data,columns=coly)
    d=dict(zip(tempx['Date'],tempx['Max Temperature']))
    d1=dict(zip(tempy['Date'],tempy['Min Temperature']))
    max_key = max(d, key = d.get)
    min_key=min(d1,key=d1.get)
    valor1=d.get(max_key)
    valor2=d1.get(min_key)
    print('La fecha de max temperatura es:',max_key,valor1)
    print('La fecha de min temperatura es:',min_key,valor2)
    diference(5)

  elif(x==6):
    data=pd.read_csv(c[5],index_col=False)
    colx=['Date','Max Temperature']
    coly=['Date','Min Temperature']
    tempx=pd.DataFrame(data,columns=colx)
    tempy=pd.DataFrame(data,columns=coly)
    d=dict(zip(tempx['Date'],tempx['Max Temperature']))
    d1=dict(zip(tempy['Date'],tempy['Min Temperature']))
    max_key = max(d, key = d.get)
    min_key=min(d1,key=d1.get)
    valor1=d.get(max_key)
    valor2=d1.get(min_key)
    print('La fecha de max temperatura es:',max_key,valor1)
    print('La fecha de min temperatura es:',min_key,valor2)
    diference(6)


  elif(x==7):
    data=pd.read_csv(c[6],index_col=False)
    colx=['Date','Max Temperature']
    coly=['Date','Min Temperature']
    tempx=pd.DataFrame(data,columns=colx)
    tempy=pd.DataFrame(data,columns=coly)
    d=dict(zip(tempx['Date'],tempx['Max Temperature']))
    d1=dict(zip(tempy['Date'],tempy['Min Temperature']))
    max_key = max(d, key = d.get)
    min_key=min(d1,key=d1.get)
    valor1=d.get(max_key)
    valor2=d1.get(min_key)
    print('La fecha de max temperatura es:',max_key,valor1)
    print('La fecha de min temperatura es:',min_key,valor2)
    diference(7)

TM(7)