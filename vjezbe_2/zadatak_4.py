import kosi_hitac_4 as k

k.kosi_hitac(30,60,0,0,0.01)
print("Maksimalna visina iznosi: {:.2f}m".format(k.maks_visina(30,60,0,0.01)))
print("Domet iznosi: {:.2f}m".format(k.domet(30,60,0,0,0.01)))
print("Maksimalna brzina iznosi: {:.2f} m/s".format(k.maks_brzina(30,60,0,0,0.01)))
k.meta(30,60,0,0,0.01,3,40,35)