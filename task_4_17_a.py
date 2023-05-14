# Известны площади круга и равностороннего треугольника. Определить:
# а) уместится ли круг в треугольнике?

import math

s_krug = float(input("введите площадь круга "))
s_treug = float(input("введите площадь треугольника "))

r_krug = (s_krug / math.pi) ** 0.5
a_treug = (4 * s_treug / 3 ** 0.5) ** 0.5
r_vpis_okr = a_treug / (2 * 3 ** 0.5)

# print(r_krug, a_treug, r_vpis_okr)
if r_krug <= r_vpis_okr:
    print("круг уместится в треугольнике")
else:
    print("круг не уместится в треугольнике")
