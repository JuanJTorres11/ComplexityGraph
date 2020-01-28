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
    for i in range(len(array)):
        array[i] = m.log(array[i], 2)
    return array


def nlog(array):
    for i in range(len(array)):
        array[i] = array[i] * m.log(array[i], 2)
    return array


def plot():
    plt.title("Grafica complejidad")
    plt.xlabel("Número de datos ingresados")
    plt.ylabel("Tiempo transcurrido")
    t = np.linspace(xpoints[0], xpoints[len(xpoints) - 1])
    plt.plot(xpoints, ypoints, 'or', label='Datos Propios')
    plt.plot(t, t, label='Lineal')
    plt.plot(t, t ** 2, label='Cuadratico')
    plt.plot(t, array_log(t), label='Logaritimico')
    plt.plot(t, nlog(t), label='Logaritimico')

    plt.show()


log(10, 10)
log(20,20)
log(30,30)
log(60,60)
plot()
