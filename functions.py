
import functools
def compras(productos,datas): 
    b =[]
    for i in productos:
        b += list(filter(lambda data:data["producto"]==i,datas))

    soloPrecios = list(map(lambda item:item["price"], b))
   
    result = functools.reduce(lambda counter,precio: counter+precio,soloPrecios )
    return soloPrecios,result
    
    
