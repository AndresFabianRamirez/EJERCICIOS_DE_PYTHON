import leercsv
import graficadora

listV = leercsv.list_diccionario('./world_population.csv')
pais1 = listV[0]

años = ['2022 Population','2020 Population','2015 Population','2010 Population','2000 Population','1990 Population','1980 Population','1970 Population']
poblacionValor = {año:poblacion for (año,poblacion) in pais1.items() if año in años}
labels = list(poblacionValor.keys())
valores = list((poblacionValor.values()))
print(valores)
valoresN = list(map(lambda i: int(i),valores))
  
graficadora.graficaBarras(labels,valoresN)








