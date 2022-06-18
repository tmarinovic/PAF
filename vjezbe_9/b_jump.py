class BungeeJumping:
    def __init__(self):
        self.x_list = []
        self.t_list = []
        self.K_list = []
        self.U_list = []
        self.Eel_list = []
        self.E_list = []
    
    def init(self,m,k,v0,h,l,oz = True,ro = 1.22,cd = 1,A = 1,dt = 0.01):
        self.m = m
        self.k = k
        self.v = v0
        self.h = h
        self.x = h
        self.l = l
        self.oz = oz
        self.ro = ro
        self.cd = cd
        self.A = A
        self.dt = dt
        self.t = 0
        self.x_list.append(self.x)
        self.t_list.append(self.t)
        self.K_list.append(0)
        self.U_list.append(m*9.81*h)
        self.Eel_list.append(0)
        self.E_list.append(m*9.81*h)

    def reset(self):
        self.m = 0
        self.k = 0
        self.v = 0        
        self.x = 0
        self.t = 0
        self.cd = 0
        self.A = 0
        self.dt = 0
        self.x_list = []
        self.t_list = []
        self.K_list = []
        self.U_list = []
        self.Eel_list = []
        self.E_list = []

    def __acc(self):
        dx = self.h - self.l - self.x
        if dx > 0:
            a_el = (self.k/self.m)*dx
        else: 
            a_el = 0
        if self.oz:
            a_oz = -(abs(self.v)*self.v*self.ro*self.cd*self.A)/(2*self.m)
        else:
            a_oz = 0
        a = -9.81 + a_el + a_oz
        return a

    def __energy(self):
        dx = self.h - self.l - self.x
        if dx > 0:
            self.Eel = (1/2)*self.k*dx*dx
        else:
            self.Eel = 0
        self.U = self.m*9.81*self.x
        self.K = (1/2)*self.m*self.v*self.v
        self.E = self.Eel + self.U + self.K

    def __jump(self):
        self.a = self.__acc()
        self.v += self.a*self.dt
        self.x += self.v*self.dt
        self.t += self.dt
        self.__energy()

    def jump(self,t):
        while self.t < t:
            self.__jump()
            self.x_list.append(self.x)
            self.t_list.append(self.t)
            self.Eel_list.append(self.Eel)
            self.K_list.append(self.K)
            self.U_list.append(self.U)
            self.E_list.append(self.E)