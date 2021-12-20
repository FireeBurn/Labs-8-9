while True:
    try:
#x1, y1, x2, y2
        x1 = int(input("Введите x координату первого поля: "))
        if x1 <= 0 or x1 > 8:
            print("Вы ввели некорректное значение")
            continue
        y1 = int(input("Введите y координату первого поля: "))
        if y1 <= 0 or y1 > 8:
            print("Вы ввели некорректное значение")
            continue
        x2 = int(input("Введите x координату второго поля: "))
        if x2 <= 0 or x2 > 8:
            print("Вы ввели некорректное значение")
            continue
        y2 = int(input("Введите y координату второго поля: "))
        if y2 <= 0 or y2 > 8:
            print("Вы ввели некорректное значение")
            continue
        print("Выберите вашу фигуру: 1 - Конь, 2 - Слон, 3 - Ладья, 4 - Ферзь")
        fig = int(input("Ваша фигруа: "))
#1 - конь, 2 - слон, 3 - ладья, 4 - ферзь
        if fig < 0 or fig > 4:
            print("Вы ввели некорректное значение")
            continue
    except ValueError:
        print("Вы ввели некорректное значение")

#1-1 8-8; 1-3 6-8 - белые с чётной суммой
#1-2 7-8; 1-4 7-8 - чёрные с нечётной
    sum1 = (x1 + y1) % 2
    sum2 = (x2 + y2) % 2
    if sum1 == sum2:
        print("Они обе", end=" ")
        if sum1 == 1:
            print("чёрного ", end="")
        else:
            print("белого ", end="")
        print("цвета")
    else:
        print("Они разных цветов")

    distx = abs(x1-x2)
    disty = abs(y1-y2)
    if fig == 1:
        if distx == 2 and disty == 1 or distx == 1 and disty == 2:
            print(f"Конь бъёт поле ({x2};{y2}) за один ход.")
        else:
            print("Не угрожает")
    elif fig == 2:
        if distx == disty:
            print(f"Слон угрожает полю({x2};{y2})")
        else:
            print("Слон не угрожает заданному полю")
#Надо отнимать от диагонали фигуры числа до тех пор, пока число не будет равно числу диагонали слона
    elif fig == 3:
        if x1 == x2 or y1 == y2:
            print(f"Ладья угрожает полю ({x2};{y2})")
        else:
            print("Ладья не угрожает данному полю")
            print(f"Для нападения переставьте фигуру на поле ({x1};{y2})")
    else:
        if distx == disty or x1 == x2 or y1 == y2:
            print(f"Ферзь угрожает полю ({x2};{y2})")
        else:
            print("Ферзь не угрожает данному полю")
            print(f"Для нападения передвиньте ферзя на поле ({x2};{y1})")

