import numpy as np 
import pandas as pd 
import argparse 
#conenedor de argumentos (el telefono entre la terminal y python)
parser = argparse.ArgumentParser(description= "programa para graficar histogramas")

parser.add_argument("media", help = "media de los datos")
parser.add_argument("desv", help= "desviacion estandar de los datos")
parser.add_argument("--n", default= 100, help= "cantidad de observaciones") # --n es lo que lo hace opcional el doble guion

args = parser.parse_args() #lleva lo que ingresaste de terminar las transforma en una variable u objeto de python como traductor

n = int(args.n)
media = float(args.media)
desv = float(args.desv)

datos = np.random.normal(size = n, loc = media, scale = desv) 
datos = datos.round(0).astype(int) 

datos_trim = [] 
for i in range(len(datos)): 
  if datos[i] <= abs(media) + 2*desv or datos[i] >= abs(media) - 2*desv: 
    datos_trim.append(datos[i]) 

datos_trim = pd.DataFrame(datos_trim) 
datos_trim.columns = ['Datos'] 
histograma = datos_trim.groupby('Datos').size() 

for i in range(len(histograma)): 
  if histograma.index[i]>=0: 
    s = "+" 
  else: 
    s = "" 
  print( 
    s, 
    histograma.index[i], 
    ' '*(1+len(str(np.max([np.max(histograma.index), 
                           abs(np.min(histograma.index))]))) - 
                           len(str(abs(histograma.index[i])))), 
    '*'*round(100*histograma.iloc[i]/len(datos_trim)), 
    sep = "" 
    )