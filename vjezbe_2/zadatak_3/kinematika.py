import matplotlib.pyplot as plt
from math import pi,sin,cos

def graph(xc,yc,xl,yl,name):
    plt.plot(xc,yc)
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.title(name)

def jednoliko_gibanje(F,m,t_t,dt):
    t_list = []
    a_list = []
    v_list = []
    s_list = []
    t = 0
    a = F/m
    v = 0
    s = 0
    t_list.append(t)
    a_list.append(a)
    v_list.append(v)
    s_list.append(s)

    while t <= t_t:
        v += a*dt
        s += v*dt
        t += dt
        t_list.append(t)
        a_list.append(a)
        v_list.append(v)
        s_list.append(s)
        
    plt.figure("Jednoliko gibanje", figsize=(8,8))
    fig = plt.subplot()
    plt.subplot(2,2,1)
    graph(t_list,a_list, "t / [s]", "a / [m/s^2]", " a-t graf")
    plt.subplot(2,2,2)
    graph(t_list,v_list, "t / [s]", "v / [m/s]", " v-t graf")
    plt.subplot(2,2,3)
    graph(t_list,s_list, "t / [s]", "s / [m]", " s-t graf")
    plt.subplots_adjust(wspace=0.5, hspace= 0.5)
    plt.show()

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

    plt.figure("Kosi hitac", figsize=(16,8))
    fig = plt.subplot()
    plt.subplot(1,2,1)
    graph(t_list,x_list,"t / [s]", "x / [m]","x - t graf")
    plt.subplot(1,2,2)
    graph(t_list,y_list,"t / [s]", "y / [m]","y - t graf")
    plt.show()
    plt.figure("Kosi hitac", figsize=(8,8))
    graph(x_list,y_list,"x / [s]", "y / [m]","x - y graf")
    plt.show()