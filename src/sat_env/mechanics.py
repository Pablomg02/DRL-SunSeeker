from .satellite import Satellite
import numpy as np

class Mechanics():
    def __init__(self, satellite : Satellite, dt : float):
        self.satellite = satellite
        self.dt = dt

    def __str__(self) -> str:
        return f'Mechanics({self.satellite}, dt: {self.dt})'

    
    def delta_velocity(self, torque):
        def ang_acceleration(torque, I):
            return torque / I
        
        k1 = ang_acceleration(torque, self.satellite.I) * self.dt
        k2 = ang_acceleration(torque, self.satellite.I) * (self.dt / 2) + k1 / 2
        k3 = ang_acceleration(torque, self.satellite.I) * (self.dt / 2) + k2 / 2
        k4 = ang_acceleration(torque, self.satellite.I) * self.dt + k3

        return (k1 + 2*k2 + 2*k3 + k4) / 6
    
    
    def delta_position(self, ang_velocity):
        return ang_velocity * self.dt
    

    def update(self, torque):
        ang_velocity = self.satellite.ang_velocity + self.delta_velocity(torque)
        ang_position = self.satellite.ang_position + self.delta_position(ang_velocity)

        if ang_position > 2*np.pi:
            ang_position = ang_position - 2*np.pi
        elif ang_position < 0:
            ang_position = ang_position + 2*np.pi
        
        self.satellite.ang_velocity = ang_velocity
        self.satellite.ang_position = ang_position
        return ang_velocity, ang_position
