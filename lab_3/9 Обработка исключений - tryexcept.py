# Задача 1: Обработка ввода числа
try:
    num = int(input("Введите число: "))
except ValueError:
    print("Ошибка: введите число!")

# Задача 2: Обработка отсутствия файла
try:
    with open("nonexistent.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Файл не найден!")