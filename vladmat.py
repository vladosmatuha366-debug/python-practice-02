

try:
    num1 = float(input("Введите первое число: "))
    operation = input("Введите операцию (+, -, *, /, //, %, ^): ").strip()
    num2 = float(input("Введите второе число: "))

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Ошибка: на ноль делить нельзя.")
            result = None
        else:
            result = num1 / num2
    elif operation == "//":
        if num2 == 0:
            print("Ошибка: на ноль делить нельзя.")
            result = None
        else:
            result = num1 // num2
    elif operation == "%":
        if num2 == 0:
            print("Ошибка: на ноль делить нельзя.")
            result = None
        else:
            result = num1 % num2
    elif operation == "^":
        result = num1 ** num2
    else:
        print("Ошибка: такой операции нет.")
        result = None

    if result is not None:
        print("Результат:", result)

except ValueError:
    print("Ошибка: введите корректное число.")
