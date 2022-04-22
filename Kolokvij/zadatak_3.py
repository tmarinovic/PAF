#upada u beskonacnu

import numpy as np
import matplotlib as plt
import math

import pd_zadatak_1 as pd

p1 = pd.projectileDrop()
p1.init(2000, 200)    
p1.gibanje(0.01)    

plt.figure("gibanje projektila")
fig = plt.subplot()
plt.subplot(2,1,1)
plt.plot(p1.t_lista,p1.h_lista_)
plt.xlabel("t [s]")
plt.ylabel("h [m]")
plt.title("h-t graf")
plt.subplot(2,1,2)
plt.plot(p1.t_lista,p1.v_lista)
plt.xlabel("t [s]")
plt.ylabel("v [m/s]")
plt.title("v-t graf")
plt.subplots_adjust(hspace = 0.6)
plt.show()



