import math as m 
import numpy as np 
import matplotlib.pyplot as plt 


class Planets:
    def __init__(self, name, color, mass, radius, r0, v0):
        self.name = name
        self.color = color
        self.mass = mass
        self.r0 = r0 
        self.v0 = v0
        self.radius = radius


class Universe:
    def __init__(self):
        self.dt = 0.0
        self.G = 6.67408 * (10**(-11))
        self.t = 0.0
        self.d = 0.0
        self.d_d = []
        self.p_planets = []
        self.S_x = []
        self.Mc_x = []
        self.V_x = []
        self.E_x = []
        self.Mr_x = []
    

    def adding(self, planet):
        self.p_planets.append(planet)


    def __acceleration(self, m1, m2, r1, r2):
        self.d = m.sqrt((r1[0] - r2[0])**2 + (r1[1] - r2[1])**2)
        return ((- self.G * m2) / (self.d**3)) * np.subtract(r1, r2)


    def evolve(self, T, dt):
        self.dt = dt
        while self.t <= T:
            for planet in self.p_planets:
                planet.a = np.array([0, 0])
                for p2 in self.p_planets:
                    if p2 == planet:
                        a = 0.0
                    else:
                        a = (self.__acceleration(planet.mass, p2.mass, planet.r0, p2.r0)) 
                        planet.a = np.add(planet.a, a)
                        self.d_d.append(self.d)
                    planet.v0 = np.add(planet.v0, planet.a * self.dt)
                    planet.r0 = np.add(planet.r0, planet.v0 * self.dt)

                    if self.d <= (planet.radius + p2.radius):
                        break
                    if planet.r0[0] <= -3e11 or planet.r0[0] >= 3e11:    
                        break
                    if planet.r0[1] <= -2.7e11 or planet.r0[1] >= 3.1e11: 
                        break

                    if p2.name == "Sun" and planet.name == "comet":
                        self.S_x.append(min(self.d_d))
                    if p2.name == "Mercury" and planet.name == "comet":
                        self.Mc_x.append(min(self.d_d))
                    if p2.name == "Venus" and planet.name == "comet":
                        self.V_x.append(min(self.d_d))
                    if p2.name == "Earth" and planet.name == "comet":
                        self.E_x.append(min(self.d_d))
                    if p2.name == "Mars" and planet.name == "comet":
                        self.Mr_x.append(min(self.d_d))

                self.d_d.clear() 
            self.t += self.dt