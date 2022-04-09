import matplotlib.pyplot as plt
import modul as m

def f1(v,x,t):
    return 10

p1 = m.Particle()
p1.init(f1,3,5,35,7,0.01)    
p1.plot_trajectory()

def f2(v,x,t):
    k = 10
    return -k*x

p2 = m.Particle()
p2.init(f2,3,5,35,7,0.01)   
p2.plot_trajectory()

def f3(v,x,t):     
    a = 3
    b = 2
    return a*x + v*t*t

p3 = m.Particle()
p3.init(f3,3,5,35,7,0.01)