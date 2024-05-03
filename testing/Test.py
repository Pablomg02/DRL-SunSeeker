import numpy as np
import matplotlib.pyplot as plt
import time

"""
    *Ecuations*
# torque = I * ang_acceleration --> ang_acceleration = torque / I
# ang_velocity = ang_velocity + ang_acceleration * dt

# ang_velocity = ang_velocity + torque * dt / I 
"""

# CONSTANTS
I = 0.2 # Inertia [kg*m^2]
ang_velocity = 0 # Angular velocity [rad/s]

ang_velocity0 = 0
ang_position0 = 0 # Angular position [rad]

dt = 0.1 # Time step [s]
max_time = 200 # Max time [s]

timesim = np.arange(0, max_time+dt, dt)
plot_dict = {"time": timesim, "ang_velocity": [], "ang_position": []}
plot_dict_RK4 = {"time": timesim, "ang_velocity": [], "ang_position": []}


# Method: Euler
def calc_ang_velocity(torque, ang_velocity, I, dt):
    ang_velocity = ang_velocity + torque * dt / I
    return ang_velocity

def calc_ang_position(ang_velocity, ang_position, dt):
    ang_position = ang_position + ang_velocity * dt
    return ang_position

# Method: Runge Kutta 4th order
def calc_ang_velocity_RK4(torque, ang_velocity, I, dt):
    def ang_acceleration(torque, I):
        return torque / I
    # Calculamos la aceleración angular en el punto inicial
    k1 = ang_acceleration(torque, I) * dt
    k2 = ang_acceleration(torque, I) * (dt / 2) + k1 / 2
    k3 = ang_acceleration(torque, I) * (dt / 2) + k2 / 2
    k4 = ang_acceleration(torque, I) * dt + k3

    ang_velocity += (k1 + 2*k2 + 2*k3 + k4) / 6
    return ang_velocity

# No se implementa el método de Runge Kutta 4th order para la posición angular




# MAIN
start_time = time.time()

for i in range(len(timesim)):
    if i == 0:
        ang_position = ang_position0
        ang_velocity = ang_velocity0
    torque = 2^(int(plot_dict["time"][i]))
    ang_velocity = calc_ang_velocity(torque, ang_velocity, I, dt)
    ang_position = calc_ang_position(ang_velocity, ang_position, dt)
    
    plot_dict["ang_velocity"].append(ang_velocity)
    plot_dict["ang_position"].append(ang_position)

print(f"Euler: {time.time() - start_time}")

start_time = time.time()
for i in range(len(timesim)):
    if i == 0:
        ang_position = ang_position0
        ang_velocity = ang_velocity0
    torque = 2^(int(plot_dict["time"][i]))
    ang_velocity = calc_ang_velocity_RK4(torque, ang_velocity, I, dt)
    ang_position = calc_ang_position(ang_velocity, ang_position, dt)
    
    plot_dict_RK4["ang_velocity"].append(ang_velocity)
    plot_dict_RK4["ang_position"].append(ang_position)

print(f"Runge Kutta 4th order: {time.time() - start_time}")



plt.plot(plot_dict["time"], plot_dict["ang_position"])
plt.plot(plot_dict_RK4["time"], plot_dict_RK4["ang_position"])
plt.show()