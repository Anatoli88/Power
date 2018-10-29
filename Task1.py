from collections import Counter

f = open('File for open.txt', 'r')

text = f.read()

print(text)

f.close()

a = text.split()

print(len(a))

print(Counter(text))

c = text.count('\n')

print(c)

f = open("File for open.txt", "r")
s = f.readlines()
f.close()
f = open("newtext.txt", "w")
# Нужно было записать строки не в обратном порядке, а первую половину переставить со второй
s.reverse()
for item in s:
    # Если ты хочешь записать строку в файл, то нужно исспользовать:
    # f.write(item)
    # В крайнем случае, можно использовать и print, но тогда это должно быть:
    # print(item, file=f)
    # но тогда у тебя появятся лишние пустые строки
    print(f, item)
f.close()
