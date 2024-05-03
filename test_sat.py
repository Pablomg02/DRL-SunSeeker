import sys

sys.path.append('src/')

import sat_env

satelite = sat_env.Satellite(I = 1, ang_position = 0, ang_velocity = 0)
sim = sat_env.Mechanics(satelite, dt = 0.1)

print(f"\nBEFORE UPDATE: {satelite}\n")
sim.update(1)
print(f"AFTER UPDATE: {satelite}")
