# Import random for random numbers
import random
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
    K_f,
    K_x,
    K_s,
    K_p,
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

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Поверхность, на которой рисуется изображение, теперь является атрибутом 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()

        # Создание поверхности для врага размером 20x10 и закрашивание ее белым цветом
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 17, 0))

        # Получение прямоугольника, описывающего положение поверхности
        # Начальное положение врага устанавливается случайным образом
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

        # Установка случайной скорости врага в пределах от 5 до 20
        self.speed = random.randint(5, 20)

    # Обновление положения спрайта на основе скорости
    # Удаление спрайта, когда он проходит левый край экрана
    def update(self):
        # Перемещение прямоугольника влево на значение скорости
        self.rect.move_ip(-self.speed, 0)
        
        # Проверка, прошел ли враг левый край экрана
        if self.rect.right < 0:
            # Удаление врага из группы спрайтов
            self.kill()

clock = pygame.time.Clock()

# Инициализация pygame
pygame.init()

# Создание объекта экрана
# Размер определяется переменными SCREEN_WIDTH и SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

# создаем эвент создания врага
ADDENEMY = pygame.USEREVENT + 1

# Создание экземпляра игрока. В настоящее время это просто прямоугольник.
player = Player()

# Создание групп для хранения спрайтов врагов и всех спрайтов
# - группа 'enemies' используется для обнаружения столкновений и обновления положения врагов
# - группа 'all_sprites' используется для отрисовки всех спрайтов
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# Добавление игрока в группу 'all_sprites'
all_sprites.add(player)


# Переменная для продолжения работы основного цикла
running = True


# runing = 1, pause = 0 
status = 0
a= 0
# Основной цикл
while running == True:
    for event in pygame.event.get():
        # keydown - нажатие клавиши
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_f:
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
            if event.key == K_x:
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))        # quit - закрыть на крестик
            if event.key == K_p:
                status = 0
            if event.key == K_s:
                status = 1
        if event.type == QUIT:
            running = False
        # новый враг?
        if event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    if status == 0:
        screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 40)
        score_text = font.render(f"Продолжить \"S\"", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

                # Обновление отображения
        pygame.display.flip()


    else:
        pygame.time.set_timer(ADDENEMY, 250)
    
        a+=1
        print("создали евент врага", a)

        # получаем последнюю нажатую клавишу
        pressed_keys = pygame.key.get_pressed()

        # обновляем позицию игрока в зависимости от нажатия клавиш пользователем
        player.update(pressed_keys)

        # обвноялем позицию врагов
        enemies.update()

        # Заполнение экрана черным цветом
        screen.fill((0, 0, 0))

        # Нарисовать все спрайты
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        # если враг столкнулся с игроком
        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            running = False

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Счет: {player.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Рисование игрока на экране
        screen.blit(player.surf, player.rect.topleft)  # вторым аргументом передается позиция игрока

        player.score += 1

        # Обновление отображения
        pygame.display.flip()

        clock.tick(20)

