import sunceIzemlja as sz
import numpy as np
import matplotlib.pyplot as plt



p = sz.SunceIZemlja()


p.init(1.989 * (10**30),5.9742 * (10**24),np.array((0,0)),np.array((0,0)),np.array((1.486*(10**11),0)),np.array((0,29783)))
p.interact(60*60*24*365.242)

plt.figure("Gravitacijska interakcija", figsize=(7,7))
ax = plt.axes()
ax.set_facecolor("black")
plt.plot(p.x_sunce,p.y_sunce, c = "yellow", label = "Sunce")
plt.plot(p.x_zemlja,p.y_zemlja, c = "blue", label = "Zemlja")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()