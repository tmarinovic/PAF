import numpy as np
import matplotlib.pyplot as plt
import math as m

class Projecttile:
    def __init__(self):
        self.vx_lista = []
        self.vy_lista = []
        self.x_lista = []
        self.y_lista = []
        self.ax_lista = []
        self.ay_lista = []
        self.t_lista = []
        
    def init(self, mass, vo, theta, xo, yo, r, Cd, stranica, dt=0.01, tijelo = 'kugla'):
        self.mass = mass
        self.vo = vo
        self.theta = theta
        self.x= xo
        self.xo = xo
        self.y = yo
        self.yo = yo
        self.r = r
        self.Cd = Cd
        self.stranica = stranica
        self.tijelo = tijelo
        self.dt = dt
        self.t = 0
        self.ax = 0
        self.ay = 0
    
        self.kut = m.radians(self.theta)
        
        self.vx = self.vo * m.cos(self.kut)
        self.vy = self.vo * m.sin(self.kut)
        
        self.vx_lista.append(self.vx)
        self.vy_lista.append(self.vy)
        self.x_lista.append(self.x)
        self.y_lista.append(self.y)
        self.ax_lista.append(self.ax)
        self.ay_lista.append(self.ay)
        self.t_lista.append(self.t)
        
        if tijelo == 'kocka':
            self.theta = abs(m.atan(self.vy/self.vx))
            self.A = stranica**2*(m.cos(self.theta) + m.sin(self.theta))
        else:
            self.A = stranica**2*m.pi

    def reset(self):
        dic = vars(self) 
        for i in dic.keys():
            dic[i] = 0
        plt.clf()
     
    def moving(self):
        a=9.81
        self.x += +self.vx*self.dt
        self.vy -= a*self.dt
        self.y += +self.vy*self.dt
        self.x_lista.append(self.x)
        self.y_lista.append(self.y)
        
    def move(self):
        while self.y >= 0:
            self.moving()
            self.t += self.dt
            self.t_lista.append(self.t)
            
        return self.x_lista, self.y_lista
    
    def acc_x(self,v,A):
        return -abs(self.vx*self.vx*self.r*self.Cd*A)/(2*self.mass)
    
    def acc_y(self, v, A):
        return -9.81-abs(self.vy*self.vy*self.r*self.Cd*A)/(2*self.mass)
    
    def gibanje(self):
        #x-smjer
        self.vx += self.ax*self.dt
        self.x += self.vx*self.dt
        #y-smjer
        self.vy += self.ay*self.dt
        self.y += self.vy*self.dt
        
        if self.tijelo == 'kocka':
            self.theta = abs(m.atan(self.vy/self.vx))
            self.A = self.stranica**2*(m.cos(self.theta) + m.sin(self.theta))
        else:
            self.A = (self.stranica**2)*math.pi
        
        self.ax = self.acc_x(self.vx, self.A)
        self.ay = self.acc_y(self.vy, self.A)
        
    def move_2(self):
        while self.y >=0:
            self.gibanje()
            self.x_lista.append(self.x)
            self.vx_lista.append(self.vx)
            self.ax_lista.append(self.ax)
            self.y_lista.append(self.y)
            self.vy_lista.append(self.vy)
            self.ay_lista.append(self.ay)
            self.t += self.dt
            self.t_lista.append(self.t)
        return self.x_lista,self.y_lista
    
    def _runge_kutta_(self):
        if self.tijelo == 'kocka':
            self.theta = abs(m.atan(self.vy/self.vx))
            self.A = self.stranica**2*(m.cos(self.theta) + m.sin(self.theta))
        else:
            self.A = (self.stranica**2)*m.pi
    
        k1vx = self.acc_x(self.vx,self.A)*self.dt 
        k1x = self.vx*self.dt
        k2vx = self.acc_x(self.vx + k1vx/2,self.A)*self.dt
        k2x = (self.vx + k1vx/2)*self.dt        
        k3vx = self.acc_x(self.vx + k2vx/2,self.A)*self.dt
        k3x = (self.vx + k2vx/2)*self.dt
        k4vx = self.acc_x(self.vx + k3vx,self.A)*self.dt
        k4x = (self.vx + k3vx)*self.dt

        self.vx += (1/6)*(k1vx + 2*k2vx + 2*k3vx + k4vx)
        self.x += (1/6)*(k1x + 2*k2x + 2*k3x + k4x)
        
        self.ax = self.acc_x(self.vx,self.A)
        

        k1vy = self.acc_y(self.vy,self.A)*self.dt 
        k1y = self.vy*self.dt
        k2vy = self.acc_y(self.vy + k1vy/2,self.A)*self.dt
        k2y = (self.vy + k1vy/2)*self.dt
        k3vy = self.acc_y(self.vy + k2vy/2,self.A)*self.dt
        k3y = (self.vy + k2vy/2)*self.dt
        k4vy = self.acc_y(self.vy + k3vy,self.A)*self.dt
        k4y = (self.vy + k3vy)*self.dt

        self.vy += (1/6)*(k1vy + 2*k2vy + 2*k3vy + k4vy)
        self.y += (1/6)*(k1y + 2*k2y + 2*k3y + k4y)

        self.ay = self.acc_y(self.vy,self.A)
        
    def runge_kutta(self):
        while self.y >=0:
            self._runge_kutta_()
            self.x_lista.append(self.x)
            self.vx_lista.append(self.vx)
            self.ax_lista.append(self.ax)
            self.y_lista.append(self.y)
            self.vy_lista.append(self.vy)
            self.ay_lista.append(self.ay)
            self.t += self.dt
            self.t_lista.append(self.t)
        return self.x_lista,self.y_lista           