import matplotlib.pyplot as plt
import numpy as np
import math

class Particle:
    def init(self,vo,theta,xo,yo,dt):
        self.vo = vo
        self.theta = theta
        self.xo = xo
        self.x = self.xo
        self.yo = yo
        self.y = self.yo
        self.dt = dt
        self.x_lista = []
        self.y_lista = []
        self.v_lista = []
        self.x_lista.append(self.x)
        self.y_lista.append(self.y)
        self.kut = self.theta*math.pi/180
        self.vx = self.vo*math.cos(self.kut)
        self.vy = self.vo*math.sin(self.kut)

    def reset(self):
        self.vo = 0
        self.theta = 0
        self.xo = 0
        self.x = 0
        self.yo = 0
        self.y = 0
        self.dt = 0
        self.x_lista = []
        self.y_lista = []
        self.v_lista = []
        self.kut = 0
        self.vx = 0
        self.vy = 0

    def __move(self):
        a = 9.81
        self.x = self.x + self.vx*self.dt
        self.v = self.vy - a*self.dt
        self.y = self.y + self.vy*self.dt
        self.x_lista.append(self.x)
        self.y_lista.append(self.y)
        self.v_initial = math.sqrt(self.vx**2 + self.vy**2)
        self.v_lista.append(self.v_initial)

    def range(self):
        while self.y >= 0:
            self.__move()
        return max(self.x_lista)

    def analiticki_domet(self):
        D = ((self.vo**2)*math.sin(2*self.kut))/9.81
        return D

    def plot_trajectory(self):
        while self.y >= 0:
            self.__move()
        plt.plot(self.x_lista,self.y_lista)
        plt.title("x-y graf")
        plt.xlabel("x[m]")
        plt.ylabel("y[m]")
        plt.show()

    def total_time(self):
        t = 0
        while self.y >= 0:
            self.__move()
            t = t + self.dt
        return t

    def max_speed(self):
        while self.y >= 0:
            self.__move()
        return max(self.v_lista)

    def velocity_to_hit_target(self,p,q,r):
        self.p = p
        self.q = q
        self.r = r
        d_lista = []
        v_lista = []

        
        pogodjena = False
        for self.vo in range(101):
            self.vx = self.vo*math.cos(self.kut)
            self.vy = self.vo*math.sin(self.kut)
            self.__move()
            domet =  math.sqrt((self.p-self.x)**2 + (self.q-self.y)**2) 
            if domet <= self.r:
                pogodena = True
                break
            else: 
                d_lista.append(domet - self.r)
                v_lista.append(self.vo)
        
        if pogodjena:
            print('Potrebna brzina za pogoditi metu je: ',self.vo)

            
            x = []
            y = []
            for fi in list(np.linspace(0,360, num = 3600)):    
                rad = fi*math.pi/180
                x_i = self.p + self.r*math.cos(rad)
                x.append(x_i)
                y_i = self.q + self.r*math.sin(rad)
                y.append(y_i)
            plt.plot(x,y)

            
            self.init(self.vo,self.theta,self.xo,self.yo,self.dt )
            self.plot_trajectory()
            self.reset()

        else:
            dom = min(d_lista)
            print("Nije moguce pogoditi metu sa zadanim kutem.")
            print('Najmanja udaljenost od mete za zadani kut iznosti: ',dom)

            indeks = d_lista.index(dom)
            v = v_lista[indeks]

            
            x = []
            y = []
            for fi in list(np.linspace(0,360, num = 3600)):    
                rad = fi*math.pi/180
                x_i = self.p + self.r*math.cos(rad)
                x.append(x_i)
                y_i = self.q + self.r*math.sin(rad)
                y.append(y_i)
            plt.plot(x,y)

            
            self.init(v,self.theta,self.x0,self.y0,self.dt )
            self.plot_trajectory()
            self.reset()
    
    def angle_to_hit_target(self,p,q,r):
        self.p = p
        self.q = q
        self.r = r
        d_lista = []
        theta_lista = []

        
        pogodjena = False
        for self.theta in range(91):
            self.kut = self.theta*math.pi/180
            self.vx = self.vo*math.cos(self.kut)
            self.vy = self.vo*math.sin(self.kut)
            self.__move()
            domet =  math.sqrt((self.mx-self.xi)**2 + (self.my-self.yi)**2) 
            if domet <= self.r:
                pogodena = True
                break
            else:
                d_lista.append(domet - self.r)
                theta_lista.append(self.theta)

        if pogodjena:
            print("Potreban kut za pogoditi metu je: °",self.theta)
            
            
            x = []
            y = []
            for fi in list(np.linspace(0,360, num = 3600)):    
                rad = fi*math.pi/180
                xi = self.p + self.r*math.cos(rad)
                x.append(xi)
                yi = self.q + self.r*math.sin(rad)
                y.append(yi)
            plt.plot(x,y)

            
            self.init(self.vo,self.theta,self.xo,self.yo,self.dt )
            self.plot_trajectory()
            self.reset()
        
        else:      
            do = min(d_lista)
            print("Nije moguce pogoditi metu sa zadanom brzinom.")
            print("Najmanja udaljenost od mete za zadanu brzinu je: ",do)
            
            indeks = d_lista.index(do)
            theta = theta_lista[indeks]

            x = []
            y = []
            for fi in list(np.linspace(0,360, num = 3600)):    
                rad = fi*math.pi/180
                xi = self.p + self.r*math.cos(rad)
                x.append(xi)
                yi = self.q + self.r*math.sin(rad)
                y.append(yi)
            plt.plot(x,y)

            self.init(self.vo,theta,self.xo,self.yo,self.dt )
            self.plot_trajectory()
            self.reset()