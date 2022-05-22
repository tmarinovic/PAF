import projectile as p 
import matplotlib.pyplot as plt 


o = p.Projecttile()
o.init(3, 30, 60, 0, 0, 1, 2, 0.15, 0.01, 'kocka')

x,y = o.runge_kutta()

b = p.Projecttile()
b.init(3, 30, 60, 0, 0, 1, 2, 0.15, 0.01, 'kugla')

q,z = b.runge_kutta()

plt.plot(x,y, label = "kocka")
plt.plot(q,z, label = "kugla")
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("x-y graf")
plt.legend()
plt.show()