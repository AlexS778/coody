import pygame

pygame.init()

SC1 = 500  # --
SC2 = 500  # |

screen = pygame.display.set_mode((SC1, SC2))
pygame.display.set_caption("Archer Defence")

image = pygame.image.load("лес.png").convert_alpha()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.exit()

    screen.blit(image, (0, 0))
    pygame.display.flip()
