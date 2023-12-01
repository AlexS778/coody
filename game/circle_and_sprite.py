# Импорт модуля pygame
import pygame

# Импорт pygame.locals для клавиш
from pygame.locals import (
    K_UP,  # клавиша вверх и тд ...
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)

# Определение констант для ширины и высоты экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Создание объекта игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # создаем Surface - картинку игрока с размером (75 на 25)
        self.surf = pygame.Surface((75, 25))
        # заполняем картинку игрока белым цветом
        self.surf.fill((255, 255, 255))
        # л
        self.rect = self.surf.get_rect()
        self.score = 0

    # Перемещение объекта игрока на экране
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:         # если клавиша вверх
            self.rect.move_ip(0, -5) 		# то двигаемся вверх по оси Y на -5
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if pressed_keys[K_SPACE]:
            self.score += 1

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


# Инициализация pygame
pygame.init()

# Создание объекта экрана
# Размер определяется переменными SCREEN_WIDTH и SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Создание экземпляра игрока. В настоящее время это просто прямоугольник.
player = Player()

# Переменная для продолжения работы основного цикла
running = True

# Основной цикл
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # получаем последнюю нажатую клавишу
    pressed_keys = pygame.key.get_pressed()

    # обновляем позицию игрока в зависимости от нажатия клавиш пользователем
    player.update(pressed_keys)

    # Заполнение экрана черным цветом
    screen.fill((0, 0, 0))

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Счет: {player.score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Рисование игрока на экране
    screen.blit(player.surf, player.rect.topleft)  # вторым аргументом передается позиция игрока

    # Обновление отображения
    pygame.display.flip()
