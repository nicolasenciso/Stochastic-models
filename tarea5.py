import matplotlib.pyplot as plt

def grafica():
    x = 0.01
    X,Y = [],[]
    while(x <= 1):
        X.append(x)
        Y.append(1-(1-x)**2)
        x = x + 0.01
    plt.plot(X,Y,color='red')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.tight_layout()
    
    plt.title('Probabilidad duelo grafica')
    plt.grid()
    plt.show()

grafica()

















