import matplotlib.pyplot as plt
import numpy as np
import math


x=int(input('unesite x: '))
y=int(input('uneiste y: '))
q,w=[int(x) for x in input('unesite koordinate sredista: ').split()]
r=int(input('unesite radijus: '))

def polozaj():
  d =math.sqrt((x-q)**2+(y-w)**2)

  if r>d:
    print("tocka se nalazi unutar kruznice")
  elif d==0:
    print("tocka se nalazi na kruznici")
  elif r<d:
    print("tocka se nalazi izvan kruzice")
polozaj()


def graf():
  
  an = np.linspace(0, 2 * np.pi, 100)
  plt.plot(3 * np.cos(an), 3 * np.sin(an))
  plt.axis('equal')

  plt.plot(x,y,'s')
  plt.show()

graf()