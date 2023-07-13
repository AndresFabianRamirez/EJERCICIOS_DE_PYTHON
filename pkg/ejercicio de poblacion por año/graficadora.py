import matplotlib.pyplot as plt
def graficaBarras(labels,valores):
    fig,ax = plt.subplots()
    ax.bar(labels,valores)
    plt.savefig('.bar.png')
    plt.close()
if __name__ =="__main__":
    labels = ["andres","pablo","maria"]
    valores = {12,4,3}
    graficaBarras()
    
