# Создание автомобиля без использования классов

# Определение характеристик автомобиля
car_color = "красный"
car_brand = "Тойота"
car_speed = 0

# Определение действий (методов) для автомобиля
def accelerate():
    global car_speed
    car_speed += 10
    print(f"Автомобиль {car_color} {car_brand} ускоряется. Скорость: {car_speed} км/ч.")

def brake():
    global car_speed
    car_speed -= 5
    if car_speed < 0:
        car_speed = 0
    print(f"Автомобиль {car_color} {car_brand} замедляется. Скорость: {car_speed} км/ч.")

# Использование характеристик и действий для автомобиля
accelerate()
brake()
