#x^2 +2bx + c = 0, b ~ u(-beta,beta), c ~ u(-beta,beta), probability to get a real root
import matplotlib.pyplot as plt

def rootProbability(step):
    b,c = -1,-1
    roots = []
    X,C,B = [], [], []
    while(b <= 1):
        B.append(b)
        b = b + step
    while(c <= 1):
        C.append(c)
        c = c + step
    size = len(B)/2
    for i in range(-size,size+1):
        X.append(i)
    Y =[]
    for i in range(0,len(X)):
        for j in range(0,len(B)):
            for k in range(0,len(C)):
                Y.append(equation(i,j,k))
                roots.append((i,b,c))
    print("LAS RAICES ENTRE: ")
    print("X : "+  str(X[0])+" y "+str(X[len(X)-1]))
    print("Con B y C entre: "+str(B[0])+" y "+str(B[len(B)-1]) + " y pasos de: "+str(step))
    print("Raices en: \n")
    for i in range(0,len(Y)-1):
        if int(Y[i]) == 0:
            print("--X-----------B------------------C")
            print(roots[i])
            print("\n")
        

def equation(x,b,c):
    output = (x**2) + (2 * b * x) + c
    return output

rootProbability(0.1)










