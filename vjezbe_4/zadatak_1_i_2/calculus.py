
def two_step(func,x,h): # h-korak
    return (func(x+h) - func(x)) / h

def three_step(func,x,h): # h-korak
    return (func(x+h) - func(x-h)) / (2*h)

def derivative(func,a,b,h,opcija):  # podrucje [a,b]
    x_lista = []
    y_lista = []
    x = a
    while x <= b:  
        x_lista.append(x)
        x += h

    if opcija == 2:    #two_step
        for x in x_lista:
            d = two_step(func,x,h)
            y_lista.append(d)
    elif opcija == 3:         #three_step
        for x in x_lista:    
            d = three_step(func,x,h)
            y_lista.append(d)

    return x_lista,y_lista

def int_pravokutnik(func,a,b,n):   # podrucje integracije [a,b] i n jednakih djelova dx
    dx = (b-a)/n 
    gornja_meda = 0
    donja_meda = 0
    c = a + dx    # za gornju medu pocinjemo od x1
    d = a    # za donju medu pocinjemo od x0
    for i in range(n):
        gornja_meda += func(c)*dx
        c += dx
        donja_meda += func(d)*dx
        d += dx
    
    return gornja_meda, donja_meda
    
def int_trapez(func,a,b,n):
    dx = (b-a)/n
    suma = 0
    x = a
    for i in range(n):
        suma += func(x)
        x += dx
    integral = suma*dx + ((func(b) + func(a))/2)*dx
    
    return integral



















