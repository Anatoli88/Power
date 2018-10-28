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
s.reverse()
for item in s:
   print(f, item)
f.close()
