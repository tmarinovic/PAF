x=int(input('unesite x: '))
y=int(input('uneiste y: '))
q,w=[int(t) for t in input('unesite koordinate sredista: ').split()]
r=int(input('unesite radijus: '))

def polozaj():
  d = r**2 - ((q-x)**2 + (w-y)**2)

  if(d>0):
    print("tocka se nalazi izvan kruznice")
  elif(d==0):
    print("tocka se nalazi na kruznici")
  else:
    print("tocka se nalazi u kruzici")
polozaj()