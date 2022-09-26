
#Найти расстояние между двумя точками пространства(числа вводятся через пробел)

print("введите координаты точки А:")
a_x, a_y = map(float, input().split())
print("введите координаты точки B:")
b_x, b_y = map(float, input().split())

dist = lambda *args: print(round(((b_x-a_x)**2 + (b_y-a_y)**2)**(0.5),3))
dist(a_x, a_y, b_x, b_y)
