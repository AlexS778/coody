class Ball:
    # создаем
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def bounce(self):
        print(f"Мяч цвета {self.color} и размера {self.size}")

ball_1 = Ball("красный", "маленький")
ball_2 = Ball("синий", "большой")

ball_1.bounce()
ball_2.bounce()

