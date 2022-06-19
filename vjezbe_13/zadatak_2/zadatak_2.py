from matplotlib import pyplot as plt
import math as m
import numpy as np
import universe 

au = 1.496e11
day = 60*60*24
year = 365.242*day

sun = universe.Planets("Sun", "yellow", 1.989e30, 0.696*1e9, np.array([0.,0.]), np.array([0.,0.]), )
mercury = universe.Planets("Mercury", "darkorange", 3.3e24, 2.439*1e6, np.array([0.,0.466 * au]), np.array([-47362.,0.]))
venus = universe.Planets("Venus", "red", 4.8685e24, 6.051*1e6, np.array([0.723 * au, 0.]), np.array([0.,35020.]))
earth = universe.Planets("Earth", "blue", 5.9742e24, 6.371*1e6, np.array([-1.*au,0.]), np.array([0.,-29783.]))
mars = universe.Planets("Mars", "brown", 6.417e23, 3.389*1e6, np.array([0., -1.666 * au]), np.array([24007., 0.]))

ss = universe.Universe()

planets = [sun, mercury, venus, earth, mars]
c_comets = []

for c in range(1000):
    mass = np.random.uniform(1.0, 9.9e13)
    radius = np.random.uniform(0.1, 0.5e3)
    position_x = np.random.uniform(1.600e11, 4*1.496e11)
    position_y = np.random.uniform(1.600e11, 4*1.496e11)
    velocity_x = np.random.uniform(-1.0e4, -4e4)
    velocity_y = np.random.uniform(-1.0e4, -4e4)
    comet = universe.Planets("comet", "black", mass, radius, np.array([position_x, position_y]), np.array([velocity_x, velocity_y]))
    c_comets.append(comet)
    ss.adding(comet)
    planets.append(comet)

    ss.adding(sun)
    ss.adding(mercury)
    ss.adding(venus)
    ss.adding(earth)
    ss.adding(mars)

    ss.evolve(5.*year, day / 10)

b = 0.175*au

S_bins = [0, b, 2*b, 3*b, 4*b, 5*b, 6*b, 7*b, 8*b, 
            9*b, 10*b, 11*b, 12*b, 13*b, 14*b, 15*b,
            16*b, 17*b, 18*b, 19*b, 20*b]

fig, axs = plt.subplots(1, 5, sharey=True, tight_layout=True)

axs[0].hist(ss.S_x, bins=S_bins)
axs[0].set_title('Sun')
axs[0].set_xlabel('distance $[au]$')
axs[0].set_ylabel('Number of comets')

axs[1].hist(ss.Mc_x, bins=S_bins)
axs[1].set_title('Mercury')
axs[1].set_xlabel('distance $[au]$')

axs[2].hist(ss.V_x, bins=S_bins)
axs[2].set_title('Venus')
axs[2].set_xlabel('distance $[au]$')

axs[3].hist(ss.E_x, bins=S_bins)
axs[3].set_title('Earth')
axs[3].set_xlabel('distance $[au]$')

axs[4].hist(ss.Mr_x, bins=S_bins)
axs[4].set_title('Mars')
axs[4].set_xlabel('distance $[au]$')

plt.show()