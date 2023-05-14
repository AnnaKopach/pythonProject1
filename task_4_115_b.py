year = int(input("введите год "))

if year >= 1984:
    year0 = year - 1984
else:
    cikl = (1984 - year) // 60
    year0 = year + (cikl + 1) * 60 - 1984

animal = year0 % 12
color = year0 % 10

if color == 0 or color == 1:
    print("зеленый")
elif color == 2 or color == 3:
    print("красный")
elif color == 4 or color == 5:
    print("желтый")
elif color == 4 or color == 5:
    print("белый")
else:
    print("черный")

if animal == 0:
    print("Крыса")
elif animal == 1:
    print("Корова")
elif animal == 2:
    print("Тигр")
elif animal == 3:
    print("Заяц")
elif animal == 4:
    print("Дракон")
elif animal == 5:
    print("Змея")
elif animal == 6:
    print("Лошадь")
elif animal == 7:
    print("Овца")
elif animal == 8:
    print("Обезьяна")
elif animal == 9:
    print("Петух")
elif animal == 10:
    print("Собака")
else:
    print("Свинья")
