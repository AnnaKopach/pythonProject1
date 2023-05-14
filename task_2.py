print("hello")

x_queen = int(input("введите координату х ферзя "))
y_queen = int(input("введите координату y ферзя "))
x_figura = int(input("введите координату х фигуры "))
y_figura = int(input("введите координату y фигуры "))

if x_figura == x_queen or y_figura == y_queen or abs(x_figura - x_queen) == abs(y_figura - y_queen):
    print("бьет")
else:
    print("не бьет")
