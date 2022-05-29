
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import EMF as emf

e = emf.EMField()
e.init(1,-1,np.array([0,0,0]),np.array([0.1,0.1,0.1]),np.array([0,0,0]),np.array([0,0,1]),0.01)  
x,y,z = e.euler(20)
e.reset()
e.init(1,-1,np.array([0,0,0]),np.array([0.1,0.1,0.1]),np.array([0,0,0]),np.array([0,0,1]),0.01)  
x_,y_,z_ = e.runge_kutta(20)

ax = plt.axes(projection = "3d")
ax.plot3D(x,y,z, c = "blue", label = "euler, dt = 0.01")
ax.plot3D(x_,y_,z_, '-.', c = "blue", label = "runge-kutta, dt = 0.01")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.view_init(30,-60)
plt.legend()
plt.show()