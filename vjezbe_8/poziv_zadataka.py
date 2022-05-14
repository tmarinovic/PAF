import Projectile as pro
import matplotlib.pyplot as plt
import numpy as np

p1 = pro.Projectile()

p1.init(84, 24, 0.5, 14, 0, 0, 0)
x1, y1 = p1.with_air_resistance_euler()
plt.plot(x1, y1, label = "Eulerova metoda")
p1.reset()

p1.init(84, 24, 0.5, 14, 0, 0, 0)
x2, y2 = p1.with_air_resistance_runge_kutta()
plt.plot(x2, y2, label = "Runge-Kutta metoda")
plt.legend()
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("x-y graf")
plt.show()
p1.reset()



#zadatak_3:
def Cd_range():
        eul = []
        rngkt= []
        Cd_cd= []
        for i in np.arange(0.0, 5.0, 0.1):
            Cd_cd.append(i)
            p1.init(84, 24, 0.5, 14, 0, 0, 0, 0.01, i, 1.28)
            e, n, = p1.with_air_resistance_euler()
            eul.append(max(e))
            p1.reset

            p1.init(84, 24, 0.5, 14, 0, 0, 0, 0.01, i, 1.28)
            r, m = p1.with_air_resistance_runge_kutta()
            rngkt.append(max(r))
            p1.reset()
                        
        plt.plot(Cd_cd, eul, label = "Eulerova metoda")
        plt.plot(Cd_cd, rngkt, label = "Runge-Kutta metoda")
        plt.legend()
        plt.title("utjecaj Cd na range")
        plt.show()

Cd_range()


def mass_range():
        eul = []
        rngkt= []
        mass= []
        for i in np.arange(0.1, 5.0, 0.1):
            mass.append(i)
            p1.init(84, 24, 0.5, i, 0, 0, 0)
            e, n= p1.with_air_resistance_euler()
            eul.append(max(e))
            p1.reset

            p1.init(84, 24, 0.5, i, 0, 0, 0)
            r, m = p1.with_air_resistance_runge_kutta()
            rngkt.append(max(r))
            p1.reset()

        plt.plot(mass, eul, label = "Eulerova metoda")
        plt.plot(mass, rngkt, label = "Runge-Kutta metoda")
        plt.legend()
        plt.title("utjecaj mase na range")
        plt.show()

mass_range()