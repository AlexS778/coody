import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Пример if/else")

color = True
if color is True:
    color = (43, 255, 0)
else:
    color = (255, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # заполнить экран черным
    screen.fill((0, 0, 0))
    # pygame.draw.rect - нарисовать квардрат на экране 
    # 1 аргументом в функцию передаем экран, на котором будем рисовать
    # 2 аргументом в функцию передаем цвет рисунка
    # 3 аргументом передаем размер рисунка
    pygame.draw.rect(screen, color, (50, 50, 100, 100))
    pygame.display.flip()
