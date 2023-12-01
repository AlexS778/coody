# Создание автомобиля с использованием класса

class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        print(f"Автомобиль {self.color} {self.brand} ускоряется. Скорость: {self.speed} км/ч.")

    def brake(self):
        self.speed -= 5
        if self.speed < 0:
            self.speed = 0
        print(f"Автомобиль {self.color} {self.brand} замедляется. Скорость: {self.speed} км/ч.")

# Использование класса для создания объектов (автомобилей)
red_car = Car("красный", "Тойота")
blue_car = Car("синий", "Форд")

# Использование объектов
red_car.accelerate()
blue_car.brake()
