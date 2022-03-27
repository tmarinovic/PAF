from numpy import absolute
import Particle as prt
import matplotlib.pyplot as plt
import math
p1 = prt.Particle()
p1.init(40, 0, 0, 80, 0.001)
domet = (40**2)*math.sin(math.radians(160))/(9.81)
print("Domet kosog hica izračun analitički jest {} metara, a numerički {} metara.".format(round(domet, 3), round(p1.range(),3)))
p1.range()
p1.trajectory()
p1.reset()

#rezultati se razlikuju a odstupanje je:
error = (domet-abs(p1.range()))/domet*100
