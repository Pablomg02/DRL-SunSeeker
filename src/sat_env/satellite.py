import numpy as np
import random

class Satellite():
    def __init__(self, I : float, 
                 ang_position : float = 0, 
                 ang_velocity : float = 0):
        
        self.I = I # Inertia [kg*m^2]
        self.ang_velocity = ang_velocity # Angular velocity [rad/s]
        self.ang_position = ang_position # Angular position [rad]

    def __str__(self) -> str:
        return f'Satellite(Inertia: {self.I}, Angular Position: {self.ang_position}, Angular Velocity: {self.ang_velocity})'


    def reset(self):
        self.ang_velocity = 0
        self.ang_position = 0


    def random_reset(self):
        self.ang_velocity = random.uniform(-1, 1)
        self.ang_position = random.uniform(0, 1)