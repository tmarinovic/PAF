import matplotlib.pyplot as plt 
import numpy as np
import math

class harmonic_oscillator:
    def __init__(self, dt, k, m, vo, xo):
        self.dt = dt
        self.k = k 
        self.m = m 
        self.vo = vo
        self.xo = xo
        self.to = 0

    def reset(self):
        dic = vars(self) 
        for i in dic.keys():
            dic[i] = 0
        plt.clf()

    def oscillate(self, total_t):
        self.t = []
        self.x = []
        self.a = []
        self.v = []
        t = 0
        
        while t < total_t:
            a = (-self.k*self.xo)/self.m
            self.vo = self.vo + a*self.dt
            self.xo = self.xo + self.vo*self.dt
            t += self.dt
            self.t.append(t)
            self.x.append(self.xo)
            self.a.append(a)
            self.v.append(self.vo)
        return(self.t, self.x)

    def plot_trajectory(self):
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
        ax1.plot(self.t, self.x, 'b')
        ax1.set_title('x-t graf')
        ax2.plot(self.t, self.v, 'b')
        ax2.set_title('v-t graf')
        ax3.plot(self.t, self.a, 'b')
        ax3.set_title('a-t graf')
        plt.pause(10)

    def analiticki(self,dt,t=2):
        self.x=[]
        self.t=[]
        self.omega=math.sqrt(self.k/self.m)
        self.to=0
        
        while self.to <= t:
            x=self.xo*math.cos(self.omega*self.to)
            self.to += dt
            self.x.append(self.xo)
            self.t.append(self.to)
        return self.x,self.t
            
    def preciznost(self,dt,total_t):
        self.oscillate(total_t)
        plt.scatter(self.t,self.x)
        plt.title('x-t graf')

    def period_titranja(self,dt,t):
        A = self.xo
        T = 0
        self.oscillate(t)
        for xi in self.x:
                if xi > 0:
                    T += dt
                else:
                    break
        return 2*T
        

    def analiticki_period(self):
        period = 2*math.pi*math.sqrt(self.m/self.k)
        print("Analiticki period titranja iznosi {}.".format(period))
        

