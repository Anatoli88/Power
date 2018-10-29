x = input('Введите строку:')

x = str(x)

a = x[::-1]

if a == x:
    print('Палиндром')
else:
    print('Не палиндром')
