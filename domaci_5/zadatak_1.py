import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import EMF as emf

def konstantno_polje(t):
    Bx = 0
    By = 0 
    Bz = 1
    return np.array((Bx,By,Bz))

def vremenski_promjenjivo_polje(t):
    Bx = 0
    By = 0
    Bz = t/10
    return np.array((Bx,By,Bz))

e = emf.EMField()
e.init(1,-1,np.array([0,0,0]),np.array([0.1,0.1,0.1]),np.array([0,0,0]),0.01,konstantno_polje)  
x,y,z = e.runge_kutta(10)

e.reset()

e.init(1,-1,np.array([0,0,0]),np.array([0.1,0.1,0.1]),np.array([0,0,0]),0.01,vremenski_promjenjivo_polje) 
x_1,y_1,z_1 = e.runge_kutta(10)

ax = plt.axes(projection = "3d")
ax.plot3D(x,y,z, label = "konstantno")
ax.plot3D(x_1,y_1,z_1, label = "vremenski promjenjivo")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("usporedba")
ax.view_init(30,40)
plt.legend(loc = "upper right")
plt.show()

p = emf.EMField()
p.init(1,1,np.array([0,0,0]),np.array([0.1,0.1,0.1]),np.array([0,0,0]),0.01,vremenski_promjenjivo_polje)  
xp,yp,zp = p.runge_kutta(10)

ax = plt.axes(projection = "3d")
ax.plot3D(x_1,y_1,z_1, label = "elektron")
ax.plot3D(xp,yp,zp, label = "pozitron")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("vremenski promjenjivo")
ax.view_init(30,40)
plt.legend(loc = "upper right")
plt.show()