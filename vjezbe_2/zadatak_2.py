import matplotlib.pyplot as plt
import numpy as np
from math import pi, sin, cos

def graph(xc,yc,xl,yl,name):
    plt.plot(xc,yc)
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.title(name)

def kosi_hitac(v0,theta,x0,y0,dt):
    g = -9.81
    th = theta*pi/180
    vx = v0*cos(th)
    vy = v0*sin(th)
    x = x0
    y = y0
    t = 0
    t_list = []
    x_list = []
    y_list = []
    t_list.append(t)
    x_list.append(x0)
    y_list.append(y0)

    while y >= 0:
        vy += g*dt 
        y += vy*dt
        x += vx*dt
        t += dt
        t_list.append(t)
        x_list.append(x)
        y_list.append(y)

    plt.figure("Grafovi", figsize=(16,8))
    fig = plt.subplot()
    plt.subplot(1,2,1)
    graph(t_list,x_list,"t / [s]", "x / [m]","x - t graf")
    plt.subplot(1,2,2)
    graph(t_list,y_list,"t / [s]", "y / [m]","y - t graf")
    plt.show()
    plt.figure(figsize=(8,8))
    graph(x_list,y_list,"x / [s]", "y / [m]","x - y graf")
    plt.show()

kosi_hitac(10,30,1,1,0.01)