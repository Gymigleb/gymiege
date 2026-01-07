'''
InfHw24_7
https://education.yandex.ru/ege/inf/task/cee8176e-48b3-474f-b2ab-b410f608fa1a
В текстовом файле набраны в разных комбинациях заглавные буквы латинского алфавита A, B, C, D, E и F.
Определите максимальное количество идущих подряд символов в прилагаемом файле, среди которых пара символов вида
гласная + согласная
(в указанном порядке) встречается не более 130 раз.
Чтобы выполнить это задание, следует написать программу.
'''

f = open("InfHw24_7.txt")

s = f.read()
s = s.strip()

for i in "AE":
    s = s.replace(i, "A")

for i in "BCDF":
    s = s.replace(i, "B")

while "AB" in s:
    s = s.replace("AB", "A B")

s = s.split()

M = 0
for i in range(len(s) - 130):
    a = sum(map(len, s[i: i + 131]))
    M = max(M, a)
print(M)