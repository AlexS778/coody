import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Пример ввода/вывода")

name = input("Enter your name: ")

font = pygame.font.Font(None, 36)
text = font.render(f"Привет, {name}!", True, (255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(text, (50, 50))
    pygame.display.flip()
