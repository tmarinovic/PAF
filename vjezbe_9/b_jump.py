import math
import numpy as np

class BungeeJumping:
    def __init__(self):
        self.x_lista = []
        self.t_lista = []
        self.K_lista = []
        self.U_lista= []
        self.Eel_lista= []
        self.E_lista = []
        
    def init(self, mass, k, vo, A, h, l, otpor_zraka = True, rho = 1.225, Cd = 1, dt= 0.01, g=9.81):
        self.mass = mass
        self.k = k
        self.vo = vo
        self.A = A
        self.h = h
        self.g = g
        self.x = h
        self.l = l
        self.otpor_zraka = otpor_zraka
        self.rho = rho
        self.Cd = Cd
        self.dt = dt
        self.t = 0
        self.x_lista.append(self.x)
        self.t_lista.append(self.t)
        self.K_lista.append(0)
        self.U_lista.append(mass*g*h)
        self.Eel_lista.append(0)
        self.E_lista.append(mass*g*h)      
        
    def reset(self):
        self.mass = 0
        self.k = 0
        self.vo = 0
        self.A = 0
        self.h = 0
        self.x = 0
        self.l = 0
        self.dt = 0
        self.x_lista = []
        self.t_lista = []
        self.K_lista = []
        self.U_lista= []
        self.Eel_lista = []
        self.E_lista = []
        
    def _acceleration_(self):
        dx = self.h - self.l - self.x
        if dx > 0:
            a_1 = (self.k/self.mass)*dx
        else:
            a_1 = 0
            
        if self.otpor_zraka:
            a_2 = -(abs(self.vo)*self.vo*self.rho*self.Cd*self.A)/(2*self.mass)
        else:
            a_2 = 0
        
        a = -self.g + a_1 + a_2
        return a
    
    def _energy_(self):
        dx = self.h - self.l - self.x
        if dx > 0:
            self.eel = (1/2)*self.k*dx*dx
        else:
            self.eel = 0
            
        self.U = self.mass*self.g*self.x
        self.K = (1/2)*self.mass*self.vo*self.vo
        self.E = self.eel + self.U + self.K
        
    def _jumping_(self):
        self.a = self._acceleration_()
        self.vo += self.a * self.dt
        self.x += self.vo * self.dt
        self.t += self.dt
        self._energy_()
        
    def _jumping_t_(self,t):
        self._jumping_()
        self.x_lista.append(self.x)
        self.t_lista.append(self.t)
        self.Eel_lista.append(self.eel)
        self.K_lista.append(self.K)
        self.U_lista.append(self.U)
        self.E_lista.append(self.E)