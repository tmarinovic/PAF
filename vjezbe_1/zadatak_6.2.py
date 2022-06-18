import matplotlib.pyplot as plt
from math import pi, sin, cos, sqrt
from numpy import linspace

def circle(xt,yt,xs,ys,r,name,save = False):
    x_list = []
    y_list = []

    d = sqrt((xt - xs)**2 + (yt - ys)**2)
    if d == r:
        print("Tocka se nalazi na kruznici.")
    elif d < r:
        print("Tocka se nalazi unutar kruznice.")
    else: 
        print("Tocka se nalazi izvan kruznice.")

    for fi in linspace(0,2*pi,num = 360):
        x = xs + r * cos(fi)
        y = ys + r * sin(fi)

        x_list.append(x)
        y_list.append(y)

    plt.plot(x_list,y_list, label = f"x^2 + y^2 = {r}")
    plt.scatter(xt,yt, s = 50, c = "orange", label = "tocka")
    plt.scatter(xs,ys, s = 50, c = "gray", label = "srediste")
    plt.title(name)
    plt.legend(loc = "lower right")
    if save:
        plt.savefig(f"{name}.pdf")
    else:
        plt.show()

circle(sqrt(2)/2,sqrt(2)/2,1,0,1,"kruznica")