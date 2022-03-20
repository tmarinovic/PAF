import matplotlib.pyplot as plt
import numpy as np
from math import *

t=np.linspace(0,10,100)
dt=0.01

def jednoliko_gibanje(sila,masa):
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
    
jednoliko_gibanje(10,7)






        



