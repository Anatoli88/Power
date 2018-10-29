import math

a = int(input("Введите сторону 1:"))
b = int(input("Введите сторону 2:"))
c = int(input("Введите сторону 3:"))

if a + b > c and b + c > a and a + c > b:
    cos_a = (a ** 2 - b ** 2 - c ** 2) / (- 2 * b * c)
    cos_b = (b ** 2 - a ** 2 - c ** 2) / (- 2 * a * c)
    cos_c = (c ** 2 - a ** 2 - b ** 2) / (- 2 * a * b)
    a = math.degrees(math.acos(cos_a))
    b = math.degrees(math.acos(cos_b))
    c = math.degrees(math.acos(cos_c))
    print("Треугольник существует")
    print('Все углы треугольника равны:')
    print('a = %f' % round(a))
    print('b = %f' % round(b))
    print('c = %f' % round(c))
else:
    print(' Такого треугольника не существует')
