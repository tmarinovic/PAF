import universe as un
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

au = 1.486*(10**11)
day = 60*60*24
year = 365.242*day

Sun = un.Planets("Sun",1.989 * (10**30),np.array((0,0)),np.array((0,0)), 'yellow') 
Mercury = un.Planets("Mercury",3.3 * (10**24),np.array((-47362,0)),np.array((0,0.466*au)), 'orange')
Venus = un.Planets("Venus",4.8685 * (10**24),np.array((0,35020)),np.array((0.723*au,0)), 'pink')
Earth = un.Planets("Earth",5.9742 * (10**24),np.array((0,-29783)),np.array((-1*au,0)), 'blue')
Mars = un.Planets("Mars",6.417 * (10**23),np.array((24007,0)),np.array((0,-1.667*au)), 'brown')

p = un.Universe() 
p.adding(Sun)
p.adding(Mercury)
p.adding(Venus)
p.adding(Earth)
p.adding(Mars)

p.interact(5*year)

plt.style.use('dark_background')

fig = plt.figure("Solar system", figsize = (8,8)) 
axis = plt.axes(xlim = (-2*au,2*au), ylim = (-2*au,2*au))

axis.plot(Sun.x_lista,Sun.y_lista, c = Sun.color, label = Sun.name, linewidth = 2)
axis.plot(Mercury.x_lista,Mercury.y_lista, c = Mercury.color, label = Mercury.name)
axis.plot(Venus.x_lista,Venus.y_lista, c = Venus.color, label = Venus.name)
axis.plot(Earth.x_lista,Earth.y_lista, c = Earth.color, label = Earth.name)
axis.plot(Mars.x_lista,Mars.y_lista, c = Mars.color, label = Mars.name)

lines = []
planets = [Sun, Mercury, Venus, Earth, Mars]


for object in planets:
    line = axis.plot([],[], "o", c = object.color)[0]
    lines.append(line)
   
def init():
    for line in lines: 
        line.set_data([], []) 
    return lines

def animate(i):
    for index, object in enumerate(planets):
        x = object.x_lista[i] 
        y = object.y_lista[i]
        lines[index].set_data(x,y) 
      
    return lines
     
anim = ani.FuncAnimation(fig, animate, init_func = init, frames = len(Earth.x_lista), interval = 10, blit = True) 

plt.axis('off') 
plt.legend(loc = "upper right")
plt.show()