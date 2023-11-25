def add_numbers(a, b):
    result = a + b
    return result

def greet(name):
    return f"Hello, {name}!"

def is_even(number):
    if number % 2 == 0:
        return True
    return False

def count_char_occurrences(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

num1 = 5
num2 = 7
sum_result = add_numbers(num1, num2)
print(f"Сумма {num1} и {num2} = {sum_result}")

person_name = "Alice"
greeting = greet(person_name)
print(greeting)

number_to_check = 10
if is_even(number_to_check):
    print(f"{number_to_check} четное число.")
else:
    print(f"{number_to_check} не четное число.")

# Using the function
temperature_in_celsius = 25
temperature_in_fahrenheit = celsius_to_fahrenheit(temperature_in_celsius)
print(f"{temperature_in_celsius} degrees Celsius is {temperature_in_fahrenheit} degrees Fahrenheit.")


# Using the function
input_string = "programming is fun"
char_to_count = "m"
occurrences = count_char_occurrences(input_string, char_to_count)
print(f"The character '{char_to_count}' appears {occurrences} times in the string.")