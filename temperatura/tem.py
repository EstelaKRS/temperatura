import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('weatherdata--548-684.csv',index_col=False)
colum=['Date','Max Temperature','Min Temperature','Solar']
temper=pd.DataFrame(data,columns=colum)
#temper.plot.line(x='Date',y=['Max Temperature','Min Temperature','Solar'],figsize=(30,10))
temper.plot.line(x='Date',y='Max Temperature',figsize=(30,10))
temper.plot.line(x='Date',y='Min Temperature',color="orange",figsize=(30,10))
temper.plot.line(x='Date',y='Solar',color="green",figsize=(30,10))
plt.show()