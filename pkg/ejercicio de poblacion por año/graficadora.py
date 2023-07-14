import matplotlib.pyplot as plt
def graficaBarras(country,labels,valores):
    fig,ax = plt.subplots()
    ax.bar(labels,valores)
    plt.savefig(f'./imgs/{country}.png')
    plt.close()
if __name__ =="__main__":
    labels = ["andres","pablo","maria"]
    valores = {12,4,3}
    graficaBarras()
    
