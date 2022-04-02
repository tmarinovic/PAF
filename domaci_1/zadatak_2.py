import matplotlib.pyplot as plt
import math 
import particle1 as prt

def ovisnost_domet_kut():
    theta_lista = []
    domet_lista = [] 

    p1 = prt.Particle()
    
    for theta in range(91):
        p1.init(10,theta,0,0,0.01)
        domet = p1.range()
        theta_lista.append(theta)
        domet_lista.append(domet)
        p1.reset()

    plt.figure("domet/kut graf")
    plt.plot(theta_lista,domet_lista)
    plt.xlabel("Kut otklona [°]")
    plt.ylabel("Domet [m]")
    plt.title("Ovisnost dometa o kutu otklona")
    plt.show()

def ovisnost_vrijeme_kut():
    theta_lista = []
    t_lista = []

    p1 = prt.Particle()

    for theta in range(91):
        p1.init(10,theta,0,0,0.01)
        t = p1.total_time()
        theta_lista.append(theta)
        t_lista.append(t)
        p1.reset()

    plt.figure("vrijeme/kut graf")
    plt.plot(theta_lista,t_lista)
    plt.xlabel("Kut otklona [°]")
    plt.ylabel("Vrijeme trajanja [s]")
    plt.title("Ovisnost vremena trajanja o kutu otklona")
    plt.show()

def ovisnot_domet_brzina():
    v_lista = []
    domet_lista = [] 

    p1 = prt.Particle()
    
    for v in range(101):
        p1.init(v,45,0,0,0.01)
        domet = p1.range()
        v_lista.append(v)
        domet_lista.append(domet)
        p1.reset()

    plt.figure("domet/brzina graf")
    plt.plot(v_lista,domet_lista)
    plt.xlabel("Iznos pocetne brzine [m/s]")
    plt.ylabel("Domet [m]")
    plt.title("Ovisnost dometa o iznosu pocetne brzine")
    plt.show()

def ovisnost_vrijeme_brzina():
    v_lista = []
    t_lista = []

    p1 = prt.Particle()

    for v in range(101):
        p1.init(v,45,0,0,0.01)
        t = p1.total_time()
        v_lista.append(v)
        t_lista.append(t)
        p1.reset()

    plt.figure("vrijeme/brzina graf")
    plt.plot(v_lista,t_lista)
    plt.xlabel("Iznos pocetne brzine [m/s]")
    plt.ylabel("Vrijeme trajanja [s]")
    plt.title("Ovisnost vremena trajanja o iznosu pocetne brzine")
    plt.show()

ovisnost_domet_kut()
ovisnost_vrijeme_kut()()
ovisnot_domet_brzina()
ovisnost_vrijeme_brzina()()
        



