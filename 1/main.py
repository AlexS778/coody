import pygame
import sys

# инициализуруем модуль pygame
pygame.init()

# создаем экран размером 400 x 300
screen = pygame.display.set_mode((400, 300))
# создаем название окошка экрана
pygame.display.set_caption("Пример ввода/вывода")

# запрашиваем имя пользователя в терминале
name = input("Введите ваше имя: ")

# создаем шрифт с размером 50
font = pygame.font.Font(None, 50)
# создаем надпись
text = font.render(f"Привет, {name}!", True, (255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("пользователь нажал на закрытие")
            pygame.quit()
            sys.exit()

    # заполянем экран с помощью функции fill
    screen.fill((0, 0, 0))
    # рисуем наш тест на экране с помощью blit
    screen.blit(text, (50, 50))
    # создаем экран
    pygame.display.flip()
