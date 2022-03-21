import numpy as np
import math
import matplotlib.pyplot as plt


def jednoliko_gibanje(sila,masa):
    t=np.linspace(0,10,100)
    dt=0.01
    a=sila/masa
    x_list=[]
    v_list=[]
    x=0
    v=0
    for i in range(100):
        v=v + a*dt
        x=x + v*dt

        x_list.append(x)
        v_list.append(v)
    fig, axs=plt.subplots(2,2)
    axs[0,0].plot(t,v_list)
    axs[0,1].plot(t,x_list)
    axs[1,0].plot(t,np.repeat(a,100))
    plt.show()

def kosi_hitac(v0, alfa, x, y):
    t=np.linspace(0,10,100)
    dt = 0.01
    vox = v0*math.cos(math.radians(alfa))
    voy = v0*math.sin(math.radians(alfa))

    vox_lista = []
    voy_lista = []
    brzina = []
    to = 0
    t_lista = []
    x_lista = []
    y_lista = []
    for i in range(100):
        to = dt*i
        t_lista.append(to)
        
        vox_lista.append(vox)
        voy = voy - 9.81*dt
        voy_lista.append(voy)
        
        v = math.sqrt(vox**2 + voy**2)
        brzina.append(v)
        x = x + vox*dt
        x_lista.append(x)
        y = y + voy*dt
        y_lista.append(y)

    plt.plot(t,x_lista)
    plt.xlabel("Vrijeme [s]")
    plt.ylabel("x [m]")
    plt.show()

    plt.plot(t,y_lista)
    plt.xlabel("Vrijeme [s]")
    plt.ylabel("y [m]")
    plt.show()

    plt.plot(t,brzina)
    plt.xlabel("Vrijeme [s]")
    plt.ylabel("Brzina [m/s]")
    plt.show()

    plt.plot(x_lista,y_lista)
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.show()


