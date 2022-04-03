import matplotlib.pyplot as plt
import math
import calculus as clc


def f1(x):
    return 5*x**3 + 2*x**2 - 8*x + 4

def der_f1(x):
    return 15*x**2 + 4*x - 8

x_lista, y_lista = clc.derivative(f1,-2,2,0.1,2)     # two_step metoda
x1_lista, y1_lista = clc.derivative(f1,-2,2,0.01,2)     # isto
f_lista = []
for x in x_lista:
    f = der_f1(x)
    f_lista.append(f)

plt.plot(x_lista, f_lista, c = "gray", label = "analitic")
plt.scatter(x_lista, y_lista, s = 3, c = "red", label = "e = 0.1")
plt.scatter(x1_lista, y1_lista, s = 3, c = "orange", label = "e = 0.01")
plt.title("Sa two_step metodom")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.legend()
plt.show()

def f2(x):
    return 6*math.sin(2*x) + 9*math.cos(x)

def der_f2(x):
    return 12*math.cos(2*x) - 9*math.sin(x)

x_lista, y_lista = clc.derivative(f2,-2,2,0.1,3)     # three_step metoda
x1_lista, y1_lista = clc.derivative(f2,-2,2,0.01,3)     # isto
f_lista = []
for x in x_lista:
    f = der_f2(x)
    f_lista.append(f)

plt.plot(x_lista, f_lista, c = "gray", label = "analitic")
plt.scatter(x_lista, y_lista, s = 3, c = "red", label = "e = 0.1")
plt.scatter(x1_lista, y1_lista, s = 3, c = "orange", label = "e = 0.01")
plt.title("Sa three_step metodom")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.legend()
plt.show()