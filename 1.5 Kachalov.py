
print("введите координаты точки А:")
a_x = float(input())
a_y = float(input())
print("введите координаты точки b:")
b_x = float(input())
b_y = float(input())

dist = ((b_x-a_x)**2 + (b_y-a_y)**2)**(0.5)
print(f'расстояние между точками равно {dist}')