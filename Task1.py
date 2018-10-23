from collections import Counter

f = open('File for open.txt', 'r')

text = f.read()

print(text)

f.close()

a = text.split()

print(len(a))

letters = 0

print(Counter(text))