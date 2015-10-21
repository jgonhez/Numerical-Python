# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 09:44:23 2015

@author: jonathan
"""

"""esta es una implementacion del codigo de vuelo de un cohete
en ascenso puramente vertical, descrito de acuerdo a las ecuaciones de movimiento
en el ejercicio del curso metodos numericos con python, aplicando como metodo de 
solucion el metodo euler de primer orden"""

import numpy as np
from matplotlib import pyplot

h = 0
ho = 0
ms = 50 #peso del coete
g = 9.81 #aceleracion de la gravedad
p = 1.091 #densidad promedio del aire
A = np.pi*0.5*0.5
ve = 325 #velocidad expulsion combustible
Cd = 0.15 #coeficiente de arrastre en el aire
mp0 = 100 #cantidad inicial de combustible
T = 100
N = int(100/0.1)+1
t = np.linspace(0,100,N)
mp = mp0


#the numpy array u, contains the different values for fuel, velocity and hegiht for all
#discretized time values
u = np.empty_like(t,dtype=np.ndarray)
u[0]=np.array([100,0,0])

def Euler(t,u):
    tiempo = 0
    for i in range(1,len(t)):
        tiempo +=0.1
        if tiempo <= 5:
            b = 20
            u[i]=u[i-1]+0.1*np.array([-20,(-(ms+u[i-1][0])*g+b*ve-0.5*p*A*Cd*u[i-1][1]*np.abs(u[i-1][1]))/(ms+u[i-1][0]),u[i-1][1]])
        else:
            b=0
            u[i]=u[i-1]+0.1*np.array([0,(-(ms)*g-0.5*p*A*Cd*u[i-1][1]*np.abs(u[i-1][1]))/(ms),u[i-1][1]])
        if u[i][2]< 0.0:
            break          


Euler(t,u)
    

altura = list()
velocidad = list()

#Here the range is up to 372 because at that index in de array u there is not more answer, the calculation
#of Euler stop because the rocket hits the ground, so beyond that index there ist just zeros, not 
#relveant information
for i in range(372):
    altura.append(u[i][2])
    velocidad.append(u[i][1])
    
#Plot of the aswer, height vs time
    
pyplot.plot(t[0:372],altura)
pyplot.title("Height vs Time for Rocket Assingment")
pyplot.xlabel("Time axis")
pyplot.ylabel("Height")
    

"""Here are the corresponding answers to the rocket problem"""

#Fuel Mass at t = 3.2 seg

print("The mass fuel at t= 3.2 seconds is : "+str(u[32][0])+" kg\n")

print("The maximun velocity is :"+str(max(velocidad))+" m/s and it happends in "+str(t[velocidad.index(max(velocidad))/10])+ " seconds at a"\
" height of "+str(altura[velocidad.index(max(velocidad))])+ " m\n")

print("The maximun height during flight is :"+str(max(altura))+ " meters and it occurs at time equal :"+str(t[altura.index(max(altura))])+ " seconds\n")

print("The Rocket hits the ground at time equals :"+str(t[altura.index(altura[-1])])+" seconds and the velocity at that"\
" moment is :"+str(velocidad[-1])+" m/s\n")