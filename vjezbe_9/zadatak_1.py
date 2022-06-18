import b_jump as bj 
import matplotlib.pyplot as plt

j1 = bj.BungeeJumping()

j1.init(100,20,0,250,50,False)    #(m,k,v0,h,l,oz = True,ro = 1.22,cd = 1,A = 1,dt = 0.01)
j1.jump(50)

plt.figure("Bungee jumping", figsize=(15, 10), dpi=80)
fig = plt.subplot()

plt.subplot(2,2,1)
plt.plot(j1.t_list,j1.x_list)
plt.xlabel("t [s]")
plt.ylabel("x [m]")
plt.title("Graf bez otpora zraka")
#plt.show()

plt.subplot(2,2,2)
plt.plot(j1.t_list, j1.E_list, label = "ukupna energija")
plt.plot(j1.t_list, j1.K_list, label = "kineticka energija")
plt.plot(j1.t_list, j1.U_list, label = "potencijalna energija")
plt.plot(j1.t_list, j1.Eel_list, label = "elasticna energija")
plt.title("Energija bez otpora zraka")
plt.legend(loc = "upper right", prop={'size': 10} )
#plt.show()

j1.reset()

j1.init(100,20,0,250,50)    #(m,k,v0,h,l,oz = True,ro = 1.22,cd = 1,A = 1,dt = 0.01)
j1.jump(50)

plt.subplot(2,2,3)
plt.plot(j1.t_list,j1.x_list)
plt.xlabel("t [s]")
plt.ylabel("x [m]")
plt.title("Graf s otporom zraka")
#plt.show()

plt.subplot(2,2,4)
plt.plot(j1.t_list, j1.E_list, label = "ukupna energija")
plt.plot(j1.t_list, j1.K_list, label = "kineticka energija")
plt.plot(j1.t_list, j1.U_list, label = "potencijalna energija")
plt.plot(j1.t_list, j1.Eel_list, label = "elasticna energija")
plt.title("Energija s otporom zraka")
plt.legend(loc = "upper right", prop={'size': 10} )
plt.show()