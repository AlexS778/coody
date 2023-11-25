import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Conditional Operator Example")

condition = False
if condition is True:
    color = (0, 255, 0)
else:
    color = (255, 0, 0)
color = (0, 255, 0) if condition else (255, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, (50, 50, 100, 100))
    pygame.display.flip()
