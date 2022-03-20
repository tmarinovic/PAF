import matplotlib.pyplot as plt
import numpy as np
from math import *

t=np.linspace(0,10,100)
dt=0.01

def kosi_hitac(v0,alfa):

    kut=alfa*np.pi/180
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
    axs[0,0].set_title('y-t graf')
    axs[0,0].set_xlabel('$t | [s]$')
    axs[0,0].set_ylabel('$y | [m]$')

    axs[0,1].plot(t,x_list)
    axs[0,1].set_title('x-t graf')
    axs[0,1].set_xlabel('$t | [s]$')
    axs[0,1].set_ylabel('$x | [m]$')

    axs[1,0].plot(y_list,x_list)
    axs[0,0].set_title('x-y graf')
    axs[0,0].set_xlabel('$y | [m]$')
    axs[0,0].set_ylabel('$x | [m]$')


    plt.show()
kosi_hitac(2,60)
