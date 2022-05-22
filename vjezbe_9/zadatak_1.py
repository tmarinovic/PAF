import b_jump as bj
import matplotlib.pyplot as plt

o_1 = bj.BungeeJumping()

o_1.init(100, 23, 0, 1, 70, 15)
o_1._jumping_t_(30)

plt.figure('BJ',figsize=(15,10), dpi=70)
fig = plt.subplot()

plt.subplot(2,2,1)
plt.plot(o_1.t_lista,o_1.x_lista)
plt.xlabel("t [s]")
plt.ylabel("x [m]")
plt.title("bez otpora zraka")

plt.subplot(2,2,2)
plt.plot(o_1.t_lista, o_1.E_lista, label = 'E_ukupno')
plt.plot(o_1.t_lista, o_1.U_lista, label = 'E_potencijalna')
plt.plot(o_1.t_lista, o_1.K_lista, label = 'E_kineticka')
plt.plot(o_1.t_lista, o_1.Eel_lista, label = 'E_elasticna')
plt.legend(loc = "upper right", prop={'size': 10})
plt.show()

o_1.reset()
 
o_1.init(100, 23, 0, 1, 70, 15)
o_1._jumping_t_(30)

plt.subplot(2,2,3)
plt.plot(o_1.t_lista,o_1.x_lista)
plt.xlabel("t [s]")
plt.ylabel("x [m]")
plt.title("s otporom zraka")

plt.subplot(2,2,4)
plt.plot(o_1.t_lista, o_1.E_lista, label = 'E_ukupno')
plt.plot(o_1.t_lista, o_1.U_lista, label = 'E_potencijalna')
plt.plot(o_1.t_lista, o_1.K_lista, label = 'E_kineticka')
plt.plot(o_1.t_lista, o_1.Eel_lista, label = 'E_elasticna')
plt.legend(loc = "upper right", prop={'size': 10} )
plt.show()
