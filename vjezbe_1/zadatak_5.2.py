import matplotlib.pyplot as plt

def line_equation(x1,y1,x2,y2, name, ispis = True, graf = False, save = True):
    x_list = []
    y_list = []
    
    k = (y2 - y1) / (x2 - x1)
    l = y1 - k*x1
    
    if ispis:
        if l == 0:
            print("Jednadzba pravca glasi: {:.2f}x".format(k))
        elif l < 0:
            print("Jednadzba pravca glasi: {:.2f}x - {:.2f}".format(k,abs(l)))
        else:
            print("Jednadzba pravca glasi: {:.2f}x + {:.2f}".format(k,l))
    else:
        pass
    
    for x in range(x1 - 2, x2 + 3):
        y = k*x + l
        x_list.append(x)
        y_list.append(y)
    
    if graf:
        if l == 0:
            naziv = "{:.2f}x".format(k)
        elif l < 0:
            naziv = "{:.2f}x - {:.2f}".format(k,abs(l))
        else:
            naziv = "{:.2f}x + {:.2f}".format(k,l)
        plt.plot(x_list, y_list, label = naziv)
        plt.scatter(x1,y1, s = 20, c = "yellow", label = "tocka 1")
        plt.scatter(x2,y2, s = 20, c = "orange", label = "tocka 2")
        plt.title(name)
        plt.legend(loc = "best")
        if save:
            plt.savefig(f"{name}.pdf")
        else:
            plt.show()
    else:
        pass

line_equation(1,5,3,2, "pravac", False, True, False)
