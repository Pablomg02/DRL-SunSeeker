import pygame
import sys
import numpy as np

sys.path.append('src/')
import sat_env

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Satélite Rotatorio")

# Configuración de colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Variables iniciales
center = (300, 200)  # Posición central del cubo en la pantalla
size = 30  # Tamaño del cubo (satélite)

# Inicializar el satélite
satelite = sat_env.Satellite(I = 1, ang_position = 0, ang_velocity = 0)
sim = sat_env.Mechanics(satelite, dt = 0.1)

# Reloj para controlar los FPS
clock = pygame.time.Clock()

# Bucle principal
running = True
time_step_counter = 0
time_steps = np.arange(0, 10, 0.1)
while running:
    # Actualizar el satélite solo cuando el contador alcance un cierto valor
    if time_step_counter >= len(time_steps):
        running = False
    else:
        torque = 0.03
        sim.update(torque)
        angle = satelite.ang_position  # Usar la posición angular del satélite
        time_step_counter += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass  # Aquí puedes agregar lo que quieras que suceda cuando se presione la tecla izquierda

    # Limpiar la pantalla
    screen.fill(BLACK)

    # Dibujar la línea
    end_x = center[0] + np.cos(np.deg2rad(angle)) * 100
    end_y = center[1] + np.sin(np.deg2rad(angle)) * 100
    pygame.draw.line(screen, RED, center, (end_x, end_y), 3)

    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar a 60 FPS
    clock.tick(60)

pygame.quit()