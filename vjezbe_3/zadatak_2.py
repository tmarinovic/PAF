import Particle as part
import matplotlib.pyplot as plt
import math
error = []
dt = []
dto = 0.001
p1 = part.Particle()
p1.init(10, 0, 0, 60, 0.01)
D = (10**2)*math.sin(math.radians(120))/9.81
print("Analitički domet jest {} m, a numerički {} m.".format(round(D,3), round(p1.range(),3)))
p1.range()
p2 = part.Particle()
for i in range(0,100):
    dto = dto + 0.001
    dt.append(dto)
for dti in dt:
    p2.init(10, 0, 0, 60, dti)
    reska = (abs(p2.range()-D)/D)*100
    error.append(reska)
    p2.reset()
plt.plot(dt, error)
plt.xlabel("vremenski interval(dt) [s]")
plt.ylabel("error/relativna greska")
plt.title("Ovisnost error/dt: ")
plt.show()