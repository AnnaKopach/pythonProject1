# В некоторых странах Дальнего Востока (Китае, Японии и др.) использовался
# (и неофициально используется в настоящее время) календарь, отличающийся
# от применяемого нами. Этот календарь представляет собой 60-летнюю цик-
# лическую систему. Каждый 60-летний цикл состоит из пяти 12-летних под-
# циклов. В каждом подцикле года носят названия животных: Крыса, Корова,
# Тигр, Заяц, Дракон, Змея, Лошадь, Овца, Обезьяна, Петух, Собака и Свинья.
# Кроме того, в названии года фигурируют цвета животных, которые связаны
# с пятью элементами природы — Деревом (зеленый), Огнем (красный), Зем-
# лей (желтый), Металлом (белый) и Водой (черный). В результате каждое жи-
# вотное (и его год) имеет символический цвет, причем цвет этот часто совер-
# шенно не совпадает с его "естественной" окраской — Тигр может быть чер-
# ным, Свинья — красной, а Лошадь — зеленой. Например, 1984 год — год
# начала очередного цикла — назывался годом Зеленой Крысы. Каждый цвет
# в цикле (начиная с зеленого) "действует" два года, поэтому через каждые
# 60 лет имя года (животное и его цвет) повторяется.
# Составить программу, которая по заданному номеру года нашей эры n печа-
# тает его название по описанному календарю в виде: "Крыса, Зеленый". Рас-
# смотреть два случая:
# а) значение n >=1984;
# б) значение n может быть любым натуральным числом.

year = int(input("введите год "))

year0 = year - 1984
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