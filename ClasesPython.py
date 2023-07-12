""" import random
marcador = {
    "pc" : 0,
    "usuario" :0
}
def reglas(entradaUsuario,entradaPc):
    if entradaUsuario == entradaPc:
        print("Empate")
    if (entradaUsuario == "papel" and entradaPc == "tijera") or (entradaUsuario =="piedra" and entradaPc == "papel") or (entradaUsuario == "tijera" and entradaPc == "piedra"):
        marcador["pc"] +=1
        print("gana este round el pc")
    else:
        marcador["usuario"]+=1
        print("gana este el usuario")


while marcador["pc"] != 2 and marcador["usuario"] != 2:
    entradaUsuario =input("Elige piedra, papel o tijera \n")
    entradaPc = random.choice(("piedra","papel","tijera"))
    reglas(entradaUsuario,entradaPc) 

if marcador["pc"]>marcador["usuario"]:
    print ("gana el pc")
else:
    print("gana el usuario") """

""" 
def message_creator(text):
   # Escribe tu solución 👇
   dicc = {
      "computadora":"Con mi computadora puedo programar usando Python",
      "celular": "En mi celular puedo aprender usando la app de Platzi",
      "cable": "¡Hay un cable en mi bota!"
   }
   if text in dicc:
      return dicc[text]
   else:
      return "Artículo no encontrado"

text = 'computadora'
response = message_creator(text)
print(response)
 """
""" 
ingredientes = ["cebolla","piña","queso"]
comidas = ["carne encebollada","pizza","buñuelo"]
almuerzoSemana = list(map(lambda ingrediente,comida: f"con {ingrediente} podemos hacer {comida}",ingredientes,comidas))
print(almuerzoSemana)

 """
""" 
items =[
    {
    "product" : "camisa",
    "precio" : 100
},
{
    "product" : "pantalon",
    "precio" : 200
},
{
    "product" : "boxer",
    "precio" : 15
}
] 
#función de orden superior MAP
def impuestos(diccionario):
    new_diccionario = diccionario.copy()
    new_diccionario["impuesto"]=new_diccionario["precio"]*0.5
    return new_diccionario
listaConImpuestos = list(map(impuestos, items))
print(listaConImpuestos)
print(items) """
#HOF FILTER
""" matches = [ """
"""   { """
"""     'home_team': 'Bolivia', """
"""     'away_team': 'Uruguay', """
"""     'home_team_score': 3, """
"""     'away_team_score': 1, """
"""     'home_team_result': 'Win' """
"""   }, """
"""   { """
"""     'home_team': 'Brazil', """
"""     'away_team': 'Mexico', """
"""     'home_team_score': 1, """
"""     'away_team_score': 1, """
"""     'home_team_result': 'Draw' """
"""   }, """
"""   { """
"""     'home_team': 'Ecuador', """
"""     'away_team': 'Venezuela', """
"""     'home_team_score': 5, """
"""     'away_team_score': 0, """
"""     'home_team_result': 'Win' """
"""   }, """
""" ] """
""" def ganador(match): """
"""     if match['home_team_result'] == "Win": """
"""         return match """
"""  """
""" equipoGanador = list(filter(ganador,matches)) """
""" print(equipoGanador) """
""" print(len(equipoGanador)) """
import time
local = time.localtime()
result = time.asctime(local)
print(result)