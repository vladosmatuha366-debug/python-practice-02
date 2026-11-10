
while True:
    try:
        num1 = float(input("\nВведите первое число: "))
        operation = input("Введите операцию: ").strip()
        num2 = float(input("Введите второе число: "))

        result = None

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Ошибка: на ноль делить нельзя.")
            else:
                result = num1 / num2
        elif operation == "//":
            if num2 == 0:
                print("Ошибка: на ноль делить нельзя.")
            else:
                result = num1 // num2
        elif operation == "%":
            if num2 == 0:
                print("Ошибка: на ноль делить нельзя.")
            else:
                result = num1 % num2
        elif operation == "^":
            result = num1 ** num2
        else:
            print("Ошибка: неизвестная операция.")

        if result is not None:
            print("Результат:", result)

    except ValueError:
        print("Ошибка: введите корректные числа.")

    while True:
        answer = input("\nХотите выполнить ещё одну операцию? (да/нет): ").strip().lower()
        if answer in ("да", "д"):
            break
        elif answer in ("нет", "н"):
            print("\nРабота программы завершена.")
            raise SystemExit
        else:
            print("Неправильный ответ. Введите «да» или «нет».")
