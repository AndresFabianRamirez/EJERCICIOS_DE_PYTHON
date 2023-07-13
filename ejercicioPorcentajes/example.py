import main
import functions

diccionarioListo = main.list_diccionario('./WORLD.csv')
usuario='South America'
diccionarioListo = list(filter(lambda x: x['Continent']==usuario,diccionarioListo))
countries = list(map(lambda x: x['Country/Territory'],diccionarioListo))
print(countries)
porcentajes = list(map(lambda x: float(x['World Population Percentage']),diccionarioListo))
print(porcentajes)

functions.graficaCircular(countries,porcentajes)


