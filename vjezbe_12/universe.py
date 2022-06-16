import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np
import math

class Planets:
    def __init__(self, name, mass, v, r, color):
        self.name = name
        self.mass = mass
        self.v = v
        self.r = r
        self.color = color
        
        self.x_lista = []
        self.y_lista = []
        self.x_lista.append(self.r[0])
        self.y_lista.append(self.r[1])

class Universe:
    def __init__(self):
        self.dt = 10**4
        self.G =  6.67408 * (10**(-11))
        self.t = 0
        self.planets = []

    def adding(self, planet):
        self.planets.append(planet)
        
    def acceleration(self, planet_1, planet_2):
        d = math.sqrt((planet_1.r[0]-planet_2.r[0])**2 + (planet_1.r[1]-planet_2.r[1])**2)
        a = -self.G * planet_2.mass/(d**3) * np.subtract(planet_1.r,planet_2.r)
        return a      
    
    def _interact_(self):
        for p in self.planets:
            p.a = np.array((0,0))
            for pi in self.planets: 
                if pi != p:
                    a = self.acceleration(p, pi)
                    p.a = np.add(p.a, a)
            p.v = np.add(p.v, p.a * self.dt)
            p.r = np.add(p.r, p.v* self.dt)
            p.x_lista.append(p.r[0])
            p.y_lista.append(p.r[1])
            
    def interact(self,t):
        while self.t <= t:
            self._interact_()
            self.t += self.dt