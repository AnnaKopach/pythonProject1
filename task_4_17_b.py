# Известны площади круга и равностороннего треугольника. Определить:
# б) уместится ли треугольник в круге?
import math

s_krug = float(input("введите площадь круга "))
s_treug = float(input("введите площадь треугольника "))

r_krug = (s_krug / math.pi) ** 0.5
a_treug = (4 * s_treug / 3 ** 0.5) ** 0.5
r_opis_okr = a_treug / (3 ** 0.5)

# print(r_krug, a_treug, r_opis_okr)
if r_opis_okr <= r_krug:
    print("треугольник уместится в круге")
else:
    print("треугольник не уместится в круге")
