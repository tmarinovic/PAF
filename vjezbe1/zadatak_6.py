from fileinput import filename
import matplotlib.pyplot as plt
import numpy as np
import math


def polozaj(x,y,q,w,r):
  d =math.sqrt((x-q)**2+(y-w)**2)

  if r>d:
    print("tocka se nalazi unutar kruznice")
  elif d==0:
    print("tocka se nalazi na kruznici")
  elif r<d:
    print("tocka se nalazi izvan kruzice")

  an = np.linspace(0, 2 * np.pi, 100)
  plt.plot(r* np.cos(an)+q, r * np.sin(an)+w)
  plt.axis('equal')
  plt.plot(x,y,'s')
  plt.show()

polozaj(2,2,3,4,5)






def spremanje():
  upit=input('zelite li spremiti? ')
  if upit=='da':
    filename=('{}.pdf'.format())
    plt.savefig(filename)
spremanje()