import numpy as np
import math

class SunceIZemlja:
    def __init__(self):
        self.x_zemlja = []
        self.y_zemlja = []
        self.x_sunce = []
        self.y_sunce = []

    def init(self,ms,mz,rs,vs,rz,vz,dt = 10**4):
        
        self.G =  6.67408 * (10**(-11))
        self.ms = ms
        self.mz = mz
        self.rs = rs
        self.vs = vs
        self.rz = rz
        self.vz = vz
        self.x_zemlja.append(rz[0])
        self.y_zemlja.append(rz[1])
        self.x_sunce.append(rs[0])
        self.y_sunce.append(rs[1])
        self.t = 0
        self.dt = dt

    def _interact_(self):

        d1 = math.sqrt((self.rs[0]-self.rz[0])**2 + (self.rs[1]-self.rz[1])**2)
        self.a1 = -self.G * self.mz/(d1**3) * np.subtract(self.rs,self.rz)
        self.vs = np.add(self.vs,self.a1*self.dt)
        self.rs = np.add(self.rs,self.vs*self.dt)
        

        d2 = math.sqrt((self.rz[0]-self.rs[0])**2 + (self.rz[1]-self.rs[1])**2)
        self.a2 = -self.G * self.ms/(d2**3) * np.subtract(self.rz,self.rs)
        self.vz = np.add(self.vz,self.a2*self.dt)
        self.rz = np.add(self.rz,self.vz*self.dt)

    def interact(self,t):
        while self.t <= t:
            self._interact_()
            self.x_zemlja.append(self.rz[0])
            self.y_zemlja.append(self.rz[1])
            self.x_sunce.append(self.rs[0])
            self.y_sunce.append(self.rs[1])
            self.t += self.dt
        #print(self.x_sj, self.y_sunce)
        return self.x_zemlja, self.y_zemlja, self.x_sunce , self.y_sunce