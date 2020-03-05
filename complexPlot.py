import matplotlib.pyplot as plt
import numpy as np
import math as m

xpoints=[]
ypoints=[]

def registrar(numero,tiempo):
    xpoints.append(numero)
    ypoints.append(tiempo)


def log(array, constante = 1):
    array2 = array.copy()
    for i in range(len(array)):
        array2[i] = m.log(array[i], 2) * constante
    return array2


def nlog(array, constante = 1):
    array2 = array.copy()
    for i in range(len(array)):
        array2[i] = array[i] * m.log(array[i], 2) * constante
    return array2


def plot(t, constante = 1):

    plt.title("Gráfica complejidad")
    plt.xlabel("Número de datos ingresados")
    plt.ylabel("Tiempo transcurrido")

    plt.plot(xpoints, ypoints, color='r', label='Datos Propios')

    plt.plot(t, np.full(t.size, constante), label='Constante')

    plt.plot(t, t * constante, label='Lineal')

    plt.plot(t, (t ** 2) * constante, linestyle=':',color='black', label='Cuadrático')

    plt.plot(t, log(t, constante), linestyle='--', color='purple', label='Logarítmico')
        
    plt.plot(t, nlog(t, constante), color='green',linestyle='-.', label='Linearítmico')
        
    plt.legend()
    plt.show()

def main():

    n = int(input ("Indique cuántas tuplas de datos ingresará\n"))

    print ("Ingresa los datos separados por comas. Ej: 5,30")
    for i in range(n):
        entrada = input()
        datos = entrada.split(",")
        registrar(float(datos[0]),float(datos[1]))

    # Crea un array con datos generados entre el inicio y final de los ingresados por el usuario
    t = np.linspace(xpoints[0], xpoints[len(xpoints) - 1]) 

    # Pregunta la constante para las graficas
    constante = float(input("Ingrese la constante para ajustar mejor sus datos (0 para terminar el programa)\n"))

    while constante != 0:
        plot(t, constante)
        constante = float(input("Ingrese la constante para ajustar mejor sus datos (0 para terminar el programa)\n"))

if __name__=='__main__':
    #test()
    main()