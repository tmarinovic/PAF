import matplotlib.pyplot as plt
import math
import calculus as clc 

def f1(x):
    return 2*x*x - 3

def int_f1(x):
    return (2/3)*x**3 - 3*x

a = 0   # granice [a,b] i broj podijela dn
b = 5
dn = 50
n_lista = []
gornja_medja = []
donja_medja = []
analiticko = []
trapez = []

for i in range(1,20):
    n_lista.append(dn*i)

for n in n_lista:
    gornja, donja = clc.int_pravokutnik(f1,a,b,n)
    gornja_medja.append(gornja)
    donja_medja.append(donja)
    integral_trapez = clc.int_trapez(f1,a,b,n)
    trapez.append(integral_trapez)
    integral_analiticko = int_f1(b) - int_f1(a)
    analiticko.append(integral_analiticko)

plt.scatter(n_lista, gornja_medja, s = 2, c = "red", label = "gornje medje")
plt.scatter(n_lista, donja_medja, s = 2, c = "orange", label = "donje medje")
plt.scatter(n_lista, trapez, s = 2, c = "green", label = "trapezna integracija")
plt.plot(n_lista, analiticko, label = "analiticki")
plt.xlabel("N koraci")
plt.ylabel("integral")
plt.legend()
plt.show()
