while True:
    expression = input("Введите выражение (например, 2 + 2): ")
    if expression.lower() == 'выход':
        break
    try:
        result = eval(expression)
        print(f"Результат: {result}")
    except:
        print("Ошибка в выражении!")