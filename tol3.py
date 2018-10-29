x = input('Введите число: ')

x = int(x)

sum = 0

for i in range(x):
    a = input('Введите число #%d: ' % (i + 1))

    a = int(a)

    if a % 3 == 0:  # следи за предупреждениями PEP8
        sum += a

print(sum)




