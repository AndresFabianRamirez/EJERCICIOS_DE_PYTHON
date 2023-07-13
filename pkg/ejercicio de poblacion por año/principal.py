import leercsv
import graficadora

listV = leercsv.list_diccionario('./WORLD.csv')
country = input("Digite el pais del cual quiere conocer su poblacion en el tiempo:")
años = ['2022 Population','2020 Population','2015 Population','2010 Population','2000 Population','1990 Population','1980 Population','1970 Population']
filtradoPais = list(filter(lambda pais: pais["Country/Territory"]==country ,listV))
print(filtradoPais)
def valores(x):
    listVacia =[]
    for i in años:
        listVacia.append(x[i])
    return listVacia
poblacionValor = list(map(valores ,filtradoPais))


labels = años
valores = poblacionValor[0]
print(valores) 
valoresN = list(map(lambda i: int(i),valores)) 
graficadora.graficaBarras(labels,valoresN) 

