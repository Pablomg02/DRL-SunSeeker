import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append('src/')

import sat_env

satelite = sat_env.Satellite(I = 1, ang_position = 0, ang_velocity = 0.2)
sim = sat_env.Mechanics(satelite, dt = 0.1)

status = {"ang_velocity": [], "ang_position": []}
status["time"] = np.arange(0, 10, 0.1)


for i in range(len(status["time"])):
    torque = 0.1
    sim.update(torque)
    status["ang_velocity"].append(satelite.ang_velocity)
    status["ang_position"].append(satelite.ang_position)

# Crear una figura y un eje polar
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Hacer un gráfico polar de la posición angular
ax.plot(status["ang_position"], status["ang_velocity"], color='r', linewidth=3)

plt.show()
    
    
