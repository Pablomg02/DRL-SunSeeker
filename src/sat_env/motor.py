class Motor():
    def __init__(self, resistance, inductance, torque_constant, inertia):
        self.resistance = resistance
        self.inductance = inductance
        self.torque_constant = torque_constant
        self.inertia = inertia
        self.current = 0
        self.angular_velocity = 0

    def apply_voltage(self, voltage, dt):
        # Calcular la corriente en función del voltaje, la resistencia y la inductancia
        d_current = (voltage - self.current * self.resistance) / self.inductance
        self.current += d_current * dt

        # Calcular el torque en función de la corriente y la constante de torque
        torque = self.current * self.torque_constant

        # Calcular la velocidad angular en función del torque y la inercia
        d_angular_velocity = torque / self.inertia
        self.angular_velocity += d_angular_velocity * dt

        return self.angular_velocity, torque