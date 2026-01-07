'''
InfHw24_2
https://education.yandex.ru/ege/inf/task/b39ab725-f1a8-4cf7-8e8e-7d94648f1468
Текстовый файл состоит не более чем из 
10**6 символов X, Y и Z. Найдите длину самой длинной цепочки символов, не содержащей подряд двух X или двух Y.
Для выполнения этого задания следует написать программу.
'''

f = open("InfHw24_2.txt")

s = f.read()

while "XX" in s:
    s = s.replace("XX", "X X")

while "YY" in s:
    s = s.replace("YY", "Y Y")


s = s.split()

print(max(map(len, s)))