x=int(input('unesite x: '))
y=int(input('unesite y: '))
q=int(input('unesite q: '))
w=int(input('uneiste w: '))

O=[x,y]
P=[q,w]

def pravac():
    k=(w-y)/(q-x)
    b=y-(k*x)
    
    if b<0:
       print('pravac koji prolazi točkama O i P je: y= ',k,'x',b)
    else:
        print('pravac koji prolazi točkama O i P je: y= ',k,'x+',b)

pravac()


