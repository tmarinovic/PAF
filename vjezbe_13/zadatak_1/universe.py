import math as m 
import numpy as np 
import matplotlib.pyplot as plt 


class Planet:


    def __init__(self, name, color, mass, radius, r0, v0):
        self.name = name
        self.color = color
        self.mass = mass
        self.r0 = r0 
        self.v0 = v0
        self.radius = radius
        self.x_x = []
        self.y_y = []


class Universe:


    def __init__(self):
        self.dt = 0.0
        self.G = 6.67408 * (10**(-11))
        self.t = 0.0
        self.d = 0.0
        self.p_planets = []


    def add_planet(self, planet):
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
                planet.v0 = np.add(planet.v0, planet.a * self.dt)
                planet.r0 = np.add(planet.r0, planet.v0 * self.dt)
                planet.x_x.append(planet.r0[0])
                planet.y_y.append(planet.r0[1])

            self.t += self.dt