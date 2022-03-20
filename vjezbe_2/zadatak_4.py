#bijedni ali vrijedni pokusaji :D

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
  a=-9.81
  y=0
  
  kut=alfa*np.pi/180
  
  vy=v0*np.sin(kut)
  
  while True:
    vy=vy + a*dt
    if vy <=0:
      break
    y= y+vy*dt
  return y
max_visina(6,45,0)

def domet(v0,alfa):
  g=-9.81
  
  kut=alfa*np.pi/180

  D=-((v0**2/g)*np.sin(2*kut))
  return D
domet(6,67)

def max_visina(v0,alfa,y):
  dt=0.01
  a=-9.81
  
  
  kut=alfa*np.pi/180
  
  vy=v0*np.sin(kut)
  
  while True:
    vy=vy + a*dt
    if vy <=0:
      break
    y= y+vy*dt
  return y
max_visina(6,45,0)

def max_brzina(v0,alfa,y):
  kut=alfa*np.pi/180

  vx=v0*np.cos(kut)
  vy=v0*np.sin(kut)

  x=0
  dt=0.01
  a=-9.81

  while True:
    x = x+ vx*dt
    vy = vy + a*dt
    y = y + vy*dt

    if y<=0:
      break

  max_v=np.sqrt(vx**2 + vy**2)
  return max_v
max_brzina(30,68,0)





















