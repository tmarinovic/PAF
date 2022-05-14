import math as m
import matplotlib.pyplot as plt
import numpy as np


class Projectile:


    def init(self, alpha, vo, S, mass, p, q, r, dt = 0.01, Cd = 0.47, rho_air = 1.225):
        self.x = 0.0
        self.y = 0.0
        self.mass = mass
        self.alpha = m.radians(alpha)
        self.vo = vo
        self.dt = dt
        self.t = 0.0
        self.ax = 0.0
        self.ay = 0.0
        self.x_x1 = []
        self.y_y1 = []
        self.x_x2 = []
        self.y_y2 = []
        self.d_d = []
        self.vx = vo * m.cos(self.alpha)
        self.vy = vo * m.sin(self.alpha)        
        self.S = S
        self.Cd = Cd
        self.rho_air = rho_air
        self.g = 9.81 
        self.p = p 
        self.q = q
        self.r = r 
        self.d = 0.0      

    def reset(self):
        self.x = 0.0
        self.y = 0.0
        self.vo = 0.0
        self.alpha = 0.0
        self.dt = 0.0
        self.vx = 0.0
        self.vy = 0.0
        self.ax = 0.0
        self.ay = 0.0
        self.p = 0.0 
        self.q = 0.0
        self.r = 0.0
        self.d = 0.0
        self.x_x1.clear()
        self.y_y1.clear()
        self.x_x2.clear()
        self.y_y2.clear()
        
        
 #zadatak_1:       
    def with_air_resistance_euler(self):
        while self.y >= 0:
            self.vx += self.ax * self.dt
            self.vy += self.ay * self.dt 
                
            self.x += self.vx * self.dt
            self.y += self.vy * self.dt
            
            self.ax = - abs((self.vx**2) * self.rho_air * self.Cd * self.S) / (2*self.mass)
            self.ay = - self.g - abs((self.vy**2) * self.rho_air * self.Cd * self.S) / (2*self.mass)
            
            self.x_x1.append(self.x)
            self.y_y1.append(self.y)
            
        return self.x_x1, self.y_y1

 #zadatak_2:
    def acceleration_x(self, vx): 
        return (- abs((self.vx**2) * self.rho_air * self.Cd * self.S) / (2*self.mass))    
    
    def acceleration_y(self, vy): 
        return (- self.g - abs((self.vy**2) * self.rho_air * self.Cd * self.S) / (2*self.mass))  
    
    def runge_kutta(self):    
        k_1vx = self.acceleration_x(self.vx) * self.dt 
        k_1x = self.vx * self.dt
        
        k_2vx = self.acceleration_x(self.vx + (k_1vx / 2)) * self.dt
        k_2x = (self.vx + k_1vx/2) * self.dt
        
        k_3vx = self.acceleration_x(self.vx + (k_2vx / 2)) * self.dt
        k_3x = (self.vx + (k_2vx / 2)) * self.dt
        
        k_4vx = self.acceleration_x(self.vx + k_3vx) * self.dt
        k_4x = (self.vx + k_3vx) * self.dt
        
        self.vx += (1/6) * (k_1vx + 2*k_2vx + 2*k_3vx + k_4vx)
        self.x += (1/6) * (k_1x + 2*k_2x + 2*k_3x + k_4x)
        
        self.x_x2.append(self.x)
        
        
        
        k_1vy = self.acceleration_y(self.vy) * self.dt 
        k_1y = self.vy * self.dt
        
        k_2vy = self.acceleration_y(self.vy + (k_1vy / 2)) * self.dt
        k_2y = (self.vy + (k_1vy / 2)) * self.dt
        
        k_3vy = self.acceleration_y(self.vy + (k_2vy / 2)) * self.dt
        k_3y = (self.vy + (k_2vy / 2)) * self.dt
        
        k_4vy = self.acceleration_y(self.vy + k_3vy) * self.dt
        k_4y = (self.vy + k_3vy) * self.dt
        
        self.vy += (1/6) * (k_1vy + 2*k_2vy + 2*k_3vy + k_4vy)
        self.y += (1/6) * (k_1y + 2*k_2y + 2*k_3y + k_4y)
        
        self.y_y2.append(self.y)  
        
    def with_air_resistance_runge_kutta(self):   
        while self.y >= 0:
            self.runge_kutta()
        return self.x_x2, self.y_y2      