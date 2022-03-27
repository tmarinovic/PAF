import math
import matplotlib.pyplot as plt
class Particle:
    g = -9.81
    def __init__(self):
        self.t_lista = []
        self.vx_lista = []
        self.vy_lista = []
        self.ay_lista = []
        self.x_lista = []
        self.y_lista = []

    def init(self, vo, xo, yo, theta, dt=0.01):
        self.t_lista.append(0)
        self.vx = (vo*math.cos(math.radians(theta)))
        self.vx_lista.append(self.vx)
        self.vy_lista.append(vo*math.sin(math.radians(theta)))
        self.ay_lista.append(self.g)
        self.x_lista.append(xo)
        self.y_lista.append(yo)
        self.dt = dt

    def reset(self):
        self.t_lista.clear()
        self.vx_lista.clear()
        self.vy_lista.clear()
        self.ay_lista.clear()
        self.x_lista.clear()
        self.y_lista.clear()


    def __move(self, i):
        self.t_lista.append(self.t_lista[i-1] + self.dt)
        self.ay_lista.append(self.g)
        self.vx_lista.append(self.vx)
        self.vy_lista.append(self.vy_lista[i-1] + self.ay_lista[i]*self.dt)
        self.x_lista.append(self.x_lista[i-1] + self.vx_lista[i]*self.dt)
        self.y_lista.append(self.y_lista[i-1] + self.vy_lista[i]*self.dt)

    def range(self):
        i = 0
        while self.y_lista[i] >= 0:
            i += 1
            self.__move(i)
        return self.x_lista[i]

    def trajectory(self):
        plt.plot(self.x_lista,self.y_lista)
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.show()