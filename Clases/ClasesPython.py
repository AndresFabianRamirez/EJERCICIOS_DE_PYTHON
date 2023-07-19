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
""" print(len(equipoGanador)) """""" 
import time
local = time.localtime()
result = time.asctime(local)
print(result) """

""" with open('./texto.txt','r+') as file: """
"""     file.read() """
"""     file.write('hola mundo \n') """
"""     file.write('soy craack \n') """
""" import csv """
""" def read_csv(path): """
"""     with open(path) as csvFile: """
"""         reader = csv.reader(csvFile,delimiter=",") """
"""         for i in reader: """
"""             print("******") """
"""             print(i) """
""" if __name__ == "__main__": """
"""     read_csv("./WORLD.csv") """


""" list = [1,2,3] """
""" b = iter(list) """
""" next(b) """
""" for i in b: """
"""     print(i) """
"""  """
#En replit funciona
""" import matplotlib.pyplot as plt """
""" def graficaBarras(): """
"""     labels = ["pescado","cerdo","pollo"] """
"""     valores = [10,20,15] """
"""     fig,ax = plt.subplots() """
"""     ax.bar(labels,valores) """
"""     plt.show() """
""" if __name__ =="__main__": """
"""     graficaBarras() """
"""  """




#EJERCICIO USANDO EL CSV

""" import csv """
"""  """
""" def list_diccionario (csvFile): """
"""     with open(csvFile) as csvFile: """
"""         reader = csv.reader(csvFile, delimiter=(',')) """
"""         header =next (reader) """
"""         listV = [] """
"""         for row in reader: """
"""             parIterable = zip(header,row) """
"""             dicTemp = {key:value for (key,value) in parIterable} """
"""             listV.append(dicTemp) """
"""     return listV """
""" listV = list_diccionario("./WORLD.csv") """
""" pais1 = listV[0] """
""" años = ['2022 Population','2020 Population','2015 Population','2010 Population','2000 Population','1990 Population','1980 Population','1970 Population'] """
""" poblacionValor = {año:poblacion for (año,poblacion) in pais1.items() if año in años} """
""" print(poblacionValor.keys()) """
"""  """
"""  """
"""  """
"""  """
""" 
a = ["1","2","56"]
aN = list(map(lambda i:int(i),a))
print(aN) """
""" try: """

""" assert  """
""" except AssertionError as error:
    print(error) """
""" a = ("a","b","c")
iterador = iter(a)
print(next(iterador))
print(type(a))
for i in iterador:
    print(i)  """
""" 
estudiantes = {
    "tipo de colegio":"privado",
    "pais": "Colombia",
    "grado": "septimo"
}
print(estudiantes.items())
for llave,valor in estudiantes.items():
    print(llave) """

""" objetivo = int (input())
epsilon = 0.01
bajo = 0.0
alto = max(1.0,objetivo)
respuesta = (alto+bajo)/2

while abs(respuesta**2 - objetivo)>=epsilon:
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    print(f'bajo: {bajo} alto: {alto}')
    respuesta = (alto+bajo)/2
print(f'la raiz cuadrada de {objetivo} es: {respuesta}')
 """

""" for i in range(0,50):
    print(2*i +1) """
""" lista1 =[]
def nones(n):
    if n==1:
        lista1.append(1)
        print (1)
        
        return 1
    if n%2 == 0:
        return nones(n-1)
    print(n)
    lista1.append(n)
    return nones(n-1)
nones(13) 

lista2 = [1,2,456,7]
lista2.sort()
print(lista2)
lista1.sort()
print(lista1)
 """
""" A = "hola"
print(A.startswith("h"))""" 
""" import unittest

def mayordeedad(edad):
    if edad>=18:
        return False
    else:
        return False
class PruebaCristal(unittest.TestCase):
    def test_mayor_edad(self):
        edad = 20
        resultado = mayordeedad(edad)
        self.assertEqual(resultado,True)
    def test_menor_edad(self):
        edad = 15
        resultado = mayordeedad(edad)
        self.assertEqual(resultado,False)

if __name__ == "__main__":
    unittest.main()
 """
""" import unittest
def dna_to_rna(dna):
    return dna.replace("T","U")

class pruebaARN( unittest.TestCase):
    def test_digitosraros(self):
        resultado = dna_to_rna("...GCTCTCTGA..*")
        self.assertEqual(resultado,"...GCUCUCUGA..*")
        
if __name__ == "__main__":
    unittest.main() """

""" def function(a):
    return a+1,a
print(type(function(5)))

 """
 #Números primos
""" """ 

""" def primos(n,lista1):
    if n ==1:
        lista1.append(1)
        return lista1
    for i in range(2,(n//2)+2):
        if n%i == 0:
            return primos(n-1)
    lista1.append(n)
    return primos(n-1)

print(primos(17,[])) 
 """
 #caracol
""" def caracol(n):
    str1 = ""
    for i in range(1,n+1):
        str1 += i
 """
""" a =[1,2,3]
a.insert(1,4)
a.append(5)
print(a) 
print(list(range(1,5))) 
for i in ([1,2,3]):
    print(i) """
""" lista =[[],[],[],[],[]]
j=1
for i in range (6,9):
    lista[j].insert(-1,i)
    j+=1
print(lista) """
""" iterador = iter([1,2,5,6])
for i in range(1,3):
    print(next(iterador))
print(list(iterador)) """

""" lista1 =[]
for i in range(5):
    lista1.append([])
lista1[1]
print(lista1)
 """
iterador=iter(range(5))
""" print(list(iterador)) """
""" for i in range(6):
    print(next(iterador))
 """
""" lista =[1,6,4,8]
lista.insert(len(lista)//2,10)
lista.insert(len(lista)//2,15)
print(lista) """


n = 15
np = int(n)
n=16

