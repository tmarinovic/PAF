import matplotlib.pyplot as plt

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
    
    
    slika=plt.plot(k,b)
    plt.show()
    return slika
pravac()

def pdf():
    pitanje=input('želite li spremiti kao pdf? ')
    if pitanje==str('da'):
        from fpdf import FPDF
        pdf = FPDF(zadatak_5.py)
        pdf.add_page()
        pdf.set_font("Arial", size=14)
        pdf.cell(200, 10, txt="", ln=1, align="L")
        pdf.output("python.pdf")
pdf()

