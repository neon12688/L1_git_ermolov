# Задача 1: Числа от 1 до 10
for i in range(1, 11):
    print(i)

# Задача 2: Числа от 1 до N
n = int(input("Введите N: "))
for i in range(1, n + 1):
    print(i)

# Задача 3: Сумма чисел от 1 до 100
sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1
print(f"Сумма: {sum}")