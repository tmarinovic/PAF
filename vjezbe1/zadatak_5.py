from fileinput import filename
import matplotlib.pyplot as plt




def pravac(x,y,q,w):
    O=[x,y]
    P=[q,w]

    k=(w-y)/(q-x)
    b=y-(k*x)
    
    if b<0:
       print('pravac koji prolazi točkama O i P je: y= ',k,'x',b)
    else:
        print('pravac koji prolazi točkama O i P je: y= ',k,'x+',b)
    
    
    plt.plot(O,P)
    plt.plot(x,y,'s')
    plt.plot(q,w,'s')
    plt.show()
    
pravac(1,2,3,4)

def pdf():
    pitanje=input('želite li spremiti kao pdf? ')
    if pitanje==('da'):
        filename=('{}.pdf'.format('ime'))
        plt.savefig(filename)
pdf()

