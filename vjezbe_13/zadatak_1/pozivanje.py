import universe as un
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

au = 1.486*(10**11)
day = 60*60*24
year = 365.242*day

Sun = un.Planet("Sun","yellow",1.989 * (10**30),np.array((0,0)),np.array((0,0))) 
Mercury = un.Planet("Mercury","orange",3.3 * (10**24),np.array((-47362,0)),np.array((0,0.466*au)))
Venus = un.Planet("Venus","red",4.8685 * (10**24),np.array((0,35020)),np.array((0.723*au,0)))
Earth = un.Planet("Earth","blue",5.9742 * (10**24),np.array((0,-29783)),np.array((-1*au,0)))
Mars = un.Planet("Mars","brown",6.417 * (10**23),np.array((24007,0)),np.array((0,-1.667*au)))
Comet = un.Planet("Comet", "gray", 10**14, np.array((20000,-15000)), np.array((-4*au,4*au)))

p = un.Universe() 
p.add_planet(Sun)
p.add_planet(Mercury)
p.add_planet(Venus)
p.add_planet(Earth)
p.add_planet(Mars)
p.add_planet(Comet)

p.interact(5*year)

plt.style.use('dark_background')
fig = plt.figure("Solar system", figsize = (8,8)) 
axis = plt.axes() 

axis.plot(Sun.x_list,Sun.y_list, c = Sun.color, label = Sun.name, linewidth = 2)
axis.plot(Mercury.x_list,Mercury.y_list, c = Mercury.color, label = Mercury.name)
axis.plot(Venus.x_list,Venus.y_list, c = Venus.color, label = Venus.name)
axis.plot(Earth.x_list,Earth.y_list, c = Earth.color, label = Earth.name)
axis.plot(Mars.x_list,Mars.y_list, c = Mars.color, label = Mars.name)
axis.plot(Comet.x_list,Comet.y_list, c = Comet.color, label = Comet.name)

lines = []
planets = [Sun, Mercury, Venus, Earth, Mars, Comet]

for obj in planets:
    line = axis.plot([],[], "o", c = obj.color)[0]
    lines.append(line)
   
def init():
    for line in lines: 
        line.set_data([], []) 
    return lines

def animate(i):
    for index, obj in enumerate(planets):
        x = obj.x_list[i] 
        y = obj.y_list[i]
        lines[index].set_data(x,y) 
      
    return lines
     
anim = animation.FuncAnimation(fig, animate, init_func = init, 
                               frames = len(Earth.x_list), interval = 10, blit = True) 

plt.axis('off') 
plt.legend(loc = "upper right")
plt.show()