import matplotlib.pyplot as plt

def nadi_jednadzbu(x1,x2,y1,y2):
    k = (y2-y1)/(x2-x1)
    l = k*(-x1) + y1 
    if l == 0:
        print(f"Jednadzba pravca glasi: y = {k}x")
    else:
        print(f"Jednadzba pravca glasi: y = {k}x + {l}")

def nacrtaj_graf(x1,x2,y1,y2):
    x = [x1,x2]
    y = [y1,y2]
    osi = plt.axes()
    osi.set_xlim([min(x)-1,max(x)+1])
    osi.set_ylim([min(y)-1,max(y)+1])
    plt.plot(x,y)
    plt.scatter(x1,y1, s=100, c="green")
    plt.scatter(x2,y2, s=100, c="red")
    pitanje = input("Zelite li  graf odmah (odgovorite 'odmah') ili u pdf-u (odgovorite 'PDF')? ")
    if pitanje == "odmah":
        plt.show()
    elif pitanje == "PDF":
        ime = input("Kako zelite nazvati graf? ")
        plt.savefig(f"{ime}.pdf")

while True:
    a = input("Unesite x koordinatu prve tocke: ")
    try:
        x1 = float(a)
        break
    except ValueError:
        print("Koordinata mora biti broj, ponovite unos.")

while True:
    b = input("Unesite y koordinatu prve tocke: ")
    try:
        y1 = float(b)
        break
    except ValueError:
        print("Koordinata mora biti broj, ponovite unos.")

while True:
    c = input("Unesite x koordinatu druge tocke: ")
    if c == a:
        print("x druge tocke mora biti razlicit od x-a prve tocke, ponovite unos.")
    else:
        try:
            x2 = float(c)
            break
        except ValueError:
            print("Koordinata mora biti broj, ponovite unos.")

while True:
    d = input("Unesite y koordinatu druge tocke: ")
    try:
        y2 = float(d)
        break
    except ValueError:
        print("Koordinata mora biti broj, ponovite unos.")

nadi_jednadzbu(x1,x2,y1,y2)
nacrtaj_graf(x1,x2,y1,y2)
