#este software simula la compra de un producto ("los productos comprados están en productos") y los productos que hay en DATAS ("los productos disponible son ilimitados")

import functools
import functions

datas = [
    {
        "producto":"arroz",
        "price" : 1200
    },
    {
        "producto":"carne",
        "price" : 16000
    },
    {
        "producto":"buñuelo",
        "price" : 2000
    }
]
productos = ["arroz","carne","arroz"]

precios, resultado =functions.compras(productos,datas)
print(precios)
print(resultado)














