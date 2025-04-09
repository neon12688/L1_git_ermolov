import random
import datetime
import math

# Задача 1: Случайное число
print(random.randint(1, 100))

# Задача 2: Текущая дата и время
print(datetime.datetime.now())

# Задача 3: Квадратный корень
num = float(input("Введите число: "))
print(f"С math: {math.sqrt(num)}")
print(f"Без math: {num ** 0.5}")