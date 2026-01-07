'''
InfHw24_1
https://education.yandex.ru/ege/inf/task/97e2f438-d6ce-4c55-95f5-8384f58faea4
Текстовый файл состоит не более чем из 
10**6 латинских букв, десятичных цифр и символов «.», «,».
Определите наибольшее натуральное число в файле, записанное десятичными цифрами.
Например, в последовательности «a23,45bfg24,131kirt16,1fff456.» максимальным является число 456.
Для выполнения этого задания следует написать программу.
'''

f = open("InfHw24_1.txt")

from string import ascii_lowercase as alph
from string import ascii_uppercase as ALPH

s = f.read()

for i in alph:
    s = s.replace(i, " ")

for i in ALPH:
    s = s.replace(i, " ")

for i in ",.":
    s = s.replace(i, " ")

s = s.split()

print(max(map(int, s)))