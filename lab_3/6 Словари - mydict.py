# Задача 1: Информация о студенте
student = {
    "имя": "Иван",
    "возраст": 20,
    "курс": 3
}
print(student)

# Задача 2: Объединение словарей
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)

# Задача 3: Проверка наличия ключа
my_dict = {"name": "Alice", "age": 25}
key = input("Введите ключ: ")
print(key in my_dict)