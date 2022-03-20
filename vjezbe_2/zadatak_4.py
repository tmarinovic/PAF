import numpy as np
import matplotlib.pyplot as plt
import math

def kosi_hitac(v0,alfa):
    t=np.linspace(0,10,100)
    dt=0.01

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
      x_list.append(x)
      y=y+voy*dt-1/2*ay*dt*dt
      y_list.append(y)

      if y<0:
          break

    fig, axs=plt.subplots(2,2)

    axs[0,0].plot(t,y_list)
    axs[0,1].plot(t,x_list)
    axs[1,0].plot(y_list,x_list)
kosi_hitac(3,6)

def max_visina(v0,alfa):
  dt=0.01
  g=-9.81
  
  kut=alfa*np.pi/180
  
  voy=v0*np.sin(kut)
  vy=voy-g*dt

  hmax=-((vy**2) / (2*g))
  return hmax
max_visina(6,45)

def domet(v0,alfa):
  dt=0.01
  g=-9.81
  
  kut=alfa*np.pi/180

  D=-((v0**2/g)*np.sin(2*kut))
domet(6,67)














