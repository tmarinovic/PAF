import matplotlib.pyplot as plt
import math

class HarmonicOscillator:
    def init(self,m,k,v0,A,dt):
        self.m = m
        self.k = k
        self.ai = (-k/m) * A 
        self.vi = v0
        self.x0 = A
        self.xi = self.x0
        self.dt = dt
        self.ti = 0
        self.t = []
        self.a = []
        self.v = []
        self.x = []
        self.t.append(self.ti)
        self.a.append(self.ai)
        self.v.append(self.vi)
        self.x.append(self.xi)

    def reset(self):
        del self.m
        del self.k
        del self.ai
        del self.vi
        del self.xi
        del self.dt
        del self.ti
        del self.t
        del self.a
        del self.v
        del self.x

    ## privatna metoda koji cini samo jedan mali pomak za vrijeme dt
    def __move(self):      
        self.vi = self.vi + self.ai * self.dt
        self.xi = self.xi + self.vi * self.dt
        self.ai = (-self.k/self.m) * self.xi
        self.ti += self.dt
        self.v.append(self.vi)
        self.x.append(self.xi)
        self.a.append(self.ai)
        self.t.append(self.ti)

    ## metoda koja racuna putanju za vrijeme koje korisnik unese
    def oscillate(self, t):
        while self.ti <= t:
            self.__move()
  
        return self.x, self.t

    def plot_trajectory(self):
        plt.figure("Harmonic oscilator")
        fig = plt.subplot()
        plt.subplot(2,2,1)
        plt.plot(self.t,self.x)
        plt.xlabel("t [s]")
        plt.ylabel("x [m]")
        plt.title("x-t graf")
        plt.subplot(2,2,2)
        plt.plot(self.t,self.v)
        plt.xlabel("t [s]")
        plt.ylabel("v [m/s]")
        plt.title("v-t graf")
        plt.subplot(2,2,3)
        plt.plot(self.t,self.a)
        plt.xlabel("t [s]")
        plt.ylabel("a [m/s^2]")
        plt.title("a-t graf")
        plt.subplots_adjust(wspace = 0.4, hspace = 0.6)
        plt.show()

    ## metoda koja analiticki racuna putanju
    def analitic_x(self,t):
        self.x = []
        self.t = []
        self.omega = math.sqrt(self.k/self.m)
        self.fi = math.pi/2
        self.ti = 0
        while self.ti <= t:
            xi = self.xi * math.sin(self.omega*self.ti + self.fi)
            self.ti += self.dt
            self.x.append(xi)
            self.t.append(self.ti)
            
        return self.x, self.t
    
    def period(self):
        T = 0
        while True:
            self.__move()
            if self.xi < 0:
                T = 0
                break
        while True:
            self.__move()
            T += self.dt
            if self.xi > 0:
                break
        return 2*T

    def period_analitic(self):
        return 2*math.pi*math.sqrt(self.m/self.k)

