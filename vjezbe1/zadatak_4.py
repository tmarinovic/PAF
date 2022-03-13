x,y=[int(s) for s in input('unesite x i y: ').split()]
q,w=[int(t) for t in input('unesite q i w: ').split()]


def pravac():
    k=(w-y)/(q-x)
    b=y-(k*x)
    
    if b<0:
       print('pravac koji prolazi točkama O i P je: y= ',k,'x',b)
    else:
        print('pravac koji prolazi točkama O i P je: y= ',k,'x+',b)

pravac()


        