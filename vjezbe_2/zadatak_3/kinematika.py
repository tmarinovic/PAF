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

def kosi_hitac(v0,alfa):

    t=np.linspace(0,10,100)
    dt=0.01

    kut=alfa*np.pi/100
    x_list=[]
    y_list=[]
    
    x=0
    y=0
    vox=0
    voy=0
    ax=0
    ay=-9.81

    for i in range(100):
      
      vox=v0*np.cos(kut)
      voy=v0*np.sin(kut)

      x=x+vox*dt
      y=y+voy*dt-1/2*ay*dt*dt

      x_list.append(x)
      y_list.append(y)

    fig, axs=plt.subplots(2,2)

    axs[0,0].plot(t,y_list)
    axs[0,1].plot(t,x_list)
    axs[1,0].plot(y_list,x_list)
    plt.show()
