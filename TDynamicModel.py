import numpy as np

class TDynamicModel:
    def __init__(self, t,state):
        self.state = state
        self.t = t

    def equations_of_motion(self, t,state):
        G = 6.67430  # Гравитационная постоянная
        M_earth = 5.972  # Масса Земли
        R_earth = 6371000  # Радиус Земли
        initial_height = 400000  # Начальная высота над 
        x, y, z, vx, vy, vz = self.state
        r = np.sqrt(x**2 + y**2 + z**2)
        ax = -G * M_earth * x / r**3
        ay = -G * M_earth * y / r**3
        az = -G * M_earth * z / r**3
        return [vx, vy, vz, ax, ay, az]



