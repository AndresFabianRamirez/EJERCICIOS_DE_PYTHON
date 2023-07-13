import matplotlib.pyplot as plt
def graficadora():
    fig, ax = plt.subplots()
    labels =["andres", "pedro"]
    values = [12,54]
    ax.pie (values, labels = labels)
    ax.axis('equal')
    plt.savefig('.pie.png')
    plt.close()

if __name__ == "__main__":
    graficadora()