import random

# Сгенерировать случайное целое число в указанном диапазоне
random_number = random.randint(1, 10)
print("Случайное Число:", random_number)

# Сгенерировать случайное число с плавающей точкой от 0 до 1
random_float = random.random()
print("Случайное Число с Плавающей Точкой:", random_float)

# Выбрать случайный элемент из последовательности (например, из списка)
my_list = [10, 20, 30, 40, 50]
random_element = random.choice(my_list)
print("Случайный Элемент из Списка:", random_element)

# Перемешать элементы последовательности (например, списка)
random.shuffle(my_list)
print("Перемешанный Список:", my_list)

# Сгенерировать случайную выборку из популяции (например, списка) без повторений
random_sample = random.sample(my_list, 2)
print("Случайная Выборка:", random_sample)
