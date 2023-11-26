# Импортируем pygame
import pygame

# Добавляем клавиши
from pygame.locals import (
    K_UP,  # клавиша вверх
    K_DOWN,  # клавиша вниз и тд....
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Ширина создаваемого окна
SCREEN_WIDTH = 800
# Высота создаваемого окна
SCREEN_HEIGHT = 600

# Инициализируем pygame
pygame.init()

# Создаем окно с шириной и высотой которую мы указали ранее
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

# запускаем главный цикл
while running:
    # слушаем эвенты которые приходят от пользователя / игры
    for event in pygame.event.get():
        # если тип эвента равняется любому нажанию клавиши
        if event.type == KEYDOWN:
            # если клавиша которую мы нажали == Escape
            if event.key == K_ESCAPE:
                # выключаем игру / останавливаем цикл
                running = False
        # если тип эвента == закрытию окошка
        elif event.type == QUIT:
            running = False

    # заполяем экран красным цветом
    screen.fill((255, 0, 0))

    # обновляем экран игры
    pygame.display.flip()

