import random

x = random.randint(1, 10)

while int(input("Введи число от 1 до 10:")) != x:
    print("Еще попытка!")
    continue
else:
    print("Правильно!")