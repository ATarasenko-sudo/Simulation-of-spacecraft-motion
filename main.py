import numpy as np
from TAbstractIntegrator import TAbstractIntegrator
import matplotlib.pyplot as plt


#Данные для начальных условий
G = 6.67430e-11  # Гравитационная постоянная
M_earth = 5.972e24  # Масса Земли
R_earth = 6371000  # Радиус Земли
initial_height = 400000  # Начальная высота над поверхностью Земли
R_earth = 6371000
tk = 20000


initial_cond = [R_earth + initial_height, 0, 0, 0, np.sqrt(G * M_earth / (R_earth + initial_height)), 0]


#Уравнения, которые надо запихнуть в отдельный класс
def equations(t, state):
    mu = 3.98603e14
    x, y, z, vx, vy, vz = state
    r = np.sqrt(x**2 + y**2 + z**2)
    ax = -mu * x / r**3
    ay = -mu * y / r**3
    az = -mu * z / r**3
    return [vx, vy, vz, ax, ay, az]





DynMod = TAbstractIntegrator(t0 = 0, tk = tk, h = 0.1, RightParts = equations, initial_cond = initial_cond)
solve = DynMod.MoveTo()

t_eval = np.linspace(0, tk, len(solve.y[0]))
x = solve.y[0]
y = solve.y[1]
z = solve.y[2]
vx = solve.y[3]
vy = solve.y[4]
vz = solve.y[5]

# Визуализация данных
plt.figure(figsize=(12, 12))

# Графики координат
plt.subplot(2, 1, 1)
plt.plot(t_eval, x - R_earth, label='X координата (метры)')
plt.plot(t_eval, y, label='Y координата (метры)')
plt.plot(t_eval, z, label='Z координата (метры)')
plt.xlabel('Время (секунды)')
plt.ylabel('Координаты (метры)')
plt.grid()
plt.legend()

# Графики скоростей
plt.subplot(2, 1, 2)
plt.plot(t_eval, vx, label='Скорость по X (м/с)')
plt.plot(t_eval, vy, label='Скорость по Y (м/с)')
plt.plot(t_eval, vz, label='Скорость по Z (м/с)')
plt.xlabel('Время (секунды)')
plt.ylabel('Скорости (м/с)')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()