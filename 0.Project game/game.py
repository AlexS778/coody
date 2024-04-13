import pygame

pygame.init()

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("любое название")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        player_image = pygame.image.load("./jet.png").convert()
        self.surf = pygame.transform.scale(player_image, (62, 25))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.x = 0
        self.rect.y = 500 // 2
        # ваш код, здоровье и тд
        self.score = 0

    # Move the sprite based on keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 500:
            self.rect.right = 500
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 500:
            self.rect.bottom = 500


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.exit()
    pygame.display.flip()
