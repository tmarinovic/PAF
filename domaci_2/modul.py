import matplotlib.pyplot as plt

class Particle:
    def init(self,func,m,xo,vo,t_uk,dt):
        self.func = func
        self.m = m
        self.xo = xo
        self.vo = vo
        self.to = 0
        self.fo = self.func(self.vo, self.xo, self.to)
        self.ao = self.fo/self.m
        self.t_uk = t_uk
        self.dt = dt
        self.t = []
        self.f = []
        self.a = []
        self.v = []
        self.x = []
        self.t.append(self.to)
        self.f.append(self.fo)
        self.a.append(self.ao)
        self.v.append(self.vo)
        self.x.append(self.xo)
    
    def reset(self):
        dic = vars(self) 
        for i in dic.keys():
            dic[i] = 0
        plt.clf()

    def move(self):
        while self.to <= self.t_uk:            
            self.to += self.dt
            self.vo = self.vo + self.ao * self.dt
            self.xo = self.xo + self.vo * self.dt
            self.fo = self.func(self.vo,self.xo,self.to)
            self.ao = self.fo/self.m
            self.t.append(self.to)
            self.v.append(self.vo)
            self.x.append(self.xo)
            self.f.append(self.fo)
            self.a.append(self.ao)

        return self.x, self.v, self.a, self.t

    def plot_trajectory(self):
        self.move()
        plt.figure("pomicanje")
        fig = plt.subplot()
        plt.subplot(2,2,1)
        plt.plot(self.t,self.x)
        plt.xlabel("t [s]")
        plt.ylabel("x [m]")
        plt.title("x-t graf")
        
        plt.subplot(2,2,2)
        plt.plot(self.t,self.v)
        plt.xlabel("t [s]")
        plt.ylabel("v [m/s]")
        plt.title("v-t graf")
        
        plt.subplot(2,2,3)
        plt.plot(self.t,self.a)
        plt.xlabel("t [s]")
        plt.ylabel("a [m/s^2]")
        plt.title("a-t graf")
        
        plt.subplot(2,2,4)
        plt.plot(self.t,self.f)
        plt.xlabel("t [s]")
        plt.ylabel("F [N]")
        plt.title("F-t graf")
        plt.subplots_adjust(wspace = 0.4, hspace = 0.6)
        plt.show()