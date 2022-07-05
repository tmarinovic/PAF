import harmonic_oscillator as ho 
import matplotlib.pyplot as plt

h1 = ho.HarmonicOscillator()

h1.init(0.1,5,0,0.3,0.01)    #(m,k,v0,A,dt)
h1.oscillate(2)
h1.plot_trajectory()
plt.scatter(h1.t,h1.x, s = 2, c = "green", label = "dt = 0.01")
h1.reset()

h1.init(0.1,5,0,0.3,0.025)    #(m,k,v0,A,dt)
h1.oscillate(2)
plt.scatter(h1.t,h1.x, s = 4, c = "orange", label = "dt = 0.025")
h1.reset()

h1.init(0.1,5,0,0.3,0.05)    #(m,k,v0,A,dt)
h1.oscillate(2)
plt.scatter(h1.t,h1.x, s = 6, label = "dt = 0.05")
h1.reset()

h1.init(0.1,5,0,0.3,0.01)    #(m,k,v0,A,dt)
h1.analitic_x(2)
plt.plot(h1.t, h1.x, c = "red", label = "analitic")
h1.reset()

plt.xlabel("t [s]")
plt.ylabel("x [m]")
plt.title("PRECIZNOST")
plt.legend(loc = "lower right")
plt.show()