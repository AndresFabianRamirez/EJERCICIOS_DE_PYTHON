""" import requests """
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()
@app.get('/')
def get_list():
    return [1,2,3]
@app.get('/contact', response_class = HTMLResponse)
def get_list():
    return '''
       <h1> RECICLA CONECTADO </h1>
       <p> primer parrafo </p>        
    '''


""" def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(type(r.text))
    categorias = r.json()
    print(categorias) """
    

if __name__ == "__main__":
    get_categories()