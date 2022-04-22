import math as m 
import numpy as np 
import matplotlib.pyplot as plt 


class projectileDrop:


    def init(self, h0, v0, dt = 0.01):
        self.h0 = h0
        self.y = h0
        self.v0 = v0 

        self.x = 0.
        self.vx = v0
        self.vy = 0.
        self.a = 0.
        self.t = 0.
        self.v = 0.
        self.dt = dt 

        

        self.x_x = []
        self.y_y = []
        self.t_t = []
        


        print("Objekt uspješno stvoren.")
        print("Početna visina: {} m".format(self.h0))
        print("Početna brzina: {} m/s".format(self.v0))


    def reset(self):
        self.h0 = 0.
        self.y = 0.
        self.v0 = 0.
        self.x = 0.
        self.vx = 0.
        self.vy = 0.
        self.a = 0.
        self.t = 0.
        self.v = 0.
        self.dt = 0. 
        self.x_x.clear()
        self.y_y.clear()
        self.t_t.clear()


    def promjena_visine(self, dh):
        self.y += dh
        print("Nova visina: {} m".format(self.y))


    def promjena_brzine(self, dv):
        self.v0 += dv 
        print("Nova brzina: {} m/s".format(self.v0))

    def gibanje(self,dt=0.01):
        g = 9.81
        self.h_lista =[]
        self.v_lista = []
        self.t_lista= []
        
        while self.h0 >= 0:
            self.v0 = self.v0 - g*dt
            self.h = self.h0 + self.v0*dt
            self.t += dt
            self.h_lista.append(self.h)
            self.v_lista.append(self.v0)
            self.t_lista.append(self.t)
        return self.h_lista, self.v_lista, self.t_lista    
    
    def total_time(self,dt=np.linspace(1,100,100)):
        self.gibanje(dt)
        t_uk = max(self.t)
        return t_uk
    