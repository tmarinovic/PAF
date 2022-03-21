import matplotlib.pyplot as plt 
import numpy as np
def pravac(x,y,q,w):

  k = round((w-y)/(q-x1),2)
  l = -k*x + y
    
  if l<0:
      print('pravac koji prolazi točkama O i P je: y= ',k,'x',l)
  else:
      print('pravac koji prolazi točkama O i P je: y= ',k,'x+',l)

while True:
    x = float(input("Unesite x: "))
    y = float(input("Unesite y: "))
    q = float(input("Unesite q: "))
    w = float(input("Unesite w: "))
    if x == q:
        print("Ponovite unos.")
    else:
        print(pravac(x,y,q,w))
        break
xpoints = np.array([x,q])
ypoints = np.array([y,w])
plt.plot(xpoints,ypoints)
plt.plot(x,y,'s')
plt.plot(q,w,'s')

def pdf():
    pitanje=input('želite li spremiti kao pdf? ')
    if pitanje==('da'):
        filename=('{}.pdf'.format('ime'))
        plt.savefig(filename)
pdf()

