import numpy as np
from scipy.integrate import solve_ivp
from scipy.integrate import OdeSolver
from TDynamicModel import TDynamicModel
class TAbstractIntegrator:

    def __init__(self, t0, tk, h, RightParts, initial_cond):
        self.t0 = t0
        self.tk = tk
        self.h = h
        self.RightParts = RightParts
        self.initial_cond = initial_cond

 

    def OneStep(self):
        return solve_ivp(self.RightParts, t_span = (self.t0, self.t0+self.h), y0 =  self.initial_cond,method='RK45')

    def MoveTo(self):
        return solve_ivp(self.RightParts, t_span=(self.t0, self.tk) , y0 = self.initial_cond, method='RK45', max_step = self.h)




