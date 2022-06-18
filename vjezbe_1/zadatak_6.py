import matplotlib.pyplot as plt
from math import sqrt, pi, sin, cos

def nacrtaj_k_i_t(sx,sy,r,tx,ty):
    x = []
    y = [] 
    for fi in range (1, 360):
        rad = fi*pi/180
        xi = sx + r*cos(rad)
        x.append(xi)
        yi = sy + r*sin(rad)
        y.append(yi)
    plt.plot(x,y)
    plt.scatter(tx,ty,s=100, c="yellow")
    pitanje = input("Zelite li  graf odmah (odgovorite 'odmah') ili u pdf-u (odgovorite 'PDF')? ")
    if pitanje == "odmah":
        plt.show()
    elif pitanje == "PDF":
        ime = input("Kako zelite nazvati graf? ")
        plt.savefig(f"{ime}.pdf")

def izracunaj_udaljenost(sx,sy,r,tx,ty):
    d = sqrt((sx - tx)**2 + (sy - ty)**2)
    if d < r:
        print("Tocka se nalazi unutar kruznice.")
        print(f"Udaljenost kruznice od tocke je {r-d}")
    elif d == r:
        print("Tocka se nalazi tocno na kruznici.")
        print("Udaljenost kruznice od tocke je 0.")
    elif d > r:
        print("Tocka se nalazi izvan kruznice.")
        print(f"Udaljenost kruznice od tocke je {d-r}")

while True:
    a = input("Unesite x koordinatu ishodista kruznice: ")
    try:
        sx = float(a)
        break
    except ValueError:
        print("Koordinata mora biti broj, ponovite unos!")

while True:
    b = input("Unesite y koordinatu ishodista kruznice: ")
    try:
        sy = float(b)
        break
    except ValueError:
        print("Koordinata mora biti broj, ponovite unos!")

while True:
    c = input("Unesite radijus kruznice: ")
    try:
        r = float(c)
        if r > 0:
            break
        else:
            print("Radijus mora biti veci od 0, ponovite unos!")
    except ValueError:
        print("Radijus mora biti broj, ponovite unos!")
    
while True:
    d = input("Unesite x koordinatu tocke: ")
    try:
        tx = float(d)
        break
    except ValueError:
        print("Koordinata mora biti broj, ponovite unos!")

while True:
    e = input("Unesite y koordinatu tocke: ")
    try:
        ty = float(e)
        break
    except ValueError:
        print("Koordinata mora biti broj, ponovite unos!")

nacrtaj_k_i_t(sx,sy,r,tx,ty)
izracunaj_udaljenost(sx,sy,r,tx,ty) 