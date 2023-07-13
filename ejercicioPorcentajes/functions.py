import matplotlib.pyplot as plt
def graficaCircular(labels,valores):
    fig,ax = plt.subplots()
    ax.pie(valores,labels=labels)
    ax.axis('equal')
    plt.savefig('.prueba.png')
    plt.close()
if __name__ =="__main__":
  labels =["andres","pedro","sam"]
  valores = [12,45,3]
  graficaCircular(labels,valores)
    
