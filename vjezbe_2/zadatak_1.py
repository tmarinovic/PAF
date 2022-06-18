import matplotlib.pyplot as plt

def graph(xc,yc,xl,yl,name):
    plt.plot(xc,yc)
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.title(name)

def calculate(F,m,x0,t_t,dt):
    t_list = []
    a_list = []
    v_list = []
    s_list = []
    t = 0
    a = F/m
    v = 0
    s = x0
    t_list.append(t)
    a_list.append(a)
    v_list.append(v)
    s_list.append(s)

    while t <= t_t:
        v += a*dt
        s += v*dt
        t += dt
        t_list.append(t)
        a_list.append(a)
        v_list.append(v)
        s_list.append(s)
        
    plt.figure("Grafovi", figsize=(8,8))
    fig = plt.subplot()
    plt.subplot(2,2,1)
    graph(t_list,a_list, "t / [s]", "a / [m/s^2]", " a-t graf")
    plt.subplot(2,2,2)
    graph(t_list,v_list, "t / [s]", "v / [m/s]", " v-t graf")
    plt.subplot(2,2,3)
    graph(t_list,s_list, "t / [s]", "s / [m]", " s-t graf")
    plt.subplots_adjust(wspace=0.5, hspace= 0.5)
    plt.show()

calculate(10,5,0,10,0.01)






        



