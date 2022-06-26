import pandas as pd
import operator
#se muestran los datos para el 1 de enero desde 1979 -2006
datos6=pd.read_csv('weatherdata-7571000.csv',index_col=False)
#datos6.head(12716)
fil=[datos6['Date'][i] for i in range (0,12716)]
tempmax=[datos6['Max Temperature'][i] for i in range (0,12716)]
tempmin=[datos6['Min Temperature'][i] for i in range (0,12716)]
temprad=[datos6['Solar'][i] for i in range (0,12716)]
pre3 = pd.DataFrame({'fecha':fil, 'tempmax': tempmax,'tempmin': tempmin,'temprad': temprad})
pre3['fecha']=pd.to_datetime(pre3['fecha'])
#prueba filtro
indices=pre3['fecha']
new=pd.DataFrame({'tempmax': tempmax,'tempmin': tempmin,'temprad': temprad},index=indices)
new.iloc[[0,365,731,1096,1461,1797,2163,2528,2885,3250,3616,3981,4346,4711,5077,5442,5807,6172,6538,6903,
          7602,7968,8333,8698,9063,9429,9794]]

