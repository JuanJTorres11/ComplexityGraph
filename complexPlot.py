import matplotlib.pyplot as plt
import numpy as np
import math as m

xpoints=[]
ypoints=[]
img = plt.imread('complexity-graph.png')

def log(x,y):
    xpoints.append(x)
    ypoints.append(y)


def array_log(array):
    array2 = array.copy()
    for i in range(len(array)):
        array2[i] = m.log(array[i], 2)
    return array2


def nlog(array):
    array2 = array.copy()
    for i in range(len(array)):
        array2[i] = array[i] * m.log(array[i], 2)
    return array2


def plot():
    plt.title("Grafica complejidad")
    plt.xlabel("Número de datos ingresados")
    plt.ylabel("Tiempo transcurrido")
    t = np.linspace(xpoints[0], xpoints[len(xpoints) - 1])
    
    print ("Los datos en x son:")
    print (t)
    plt.plot(xpoints, ypoints, 'or', label='Datos Propios')
    plt.plot(t, t, label='Lineal')
    plt.plot(t, t ** 2, label='Cuadratico')
    print ("Los datos cuadraticos son: \n")
    print ( t**2)
    plt.plot(t, array_log(t), label='Logaritimico')
    print ("Los datos logaritmicos son: \n")
    print (array_log(t))
    plt.plot(t, nlog(t), label='n * Logaritimico')
    print ("Los datos n*log son: \n")
    print (nlog(t))

    plt.show()


log(10, 90)
log(20,420)
log(30,850)
log(60,3700)
plot()
