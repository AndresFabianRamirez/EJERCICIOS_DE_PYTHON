try: 
    print('hola')
    a = 10
    if a>5:
        print('hola')
    c = 10/0
    age =15
    if (age<18):
        raise Exception('No se permiten menores')

except NameError as error:
    print(error)
except ZeroDivisionError as error:
    print(error)
except Exception as error:
    print('No se permiten menores')