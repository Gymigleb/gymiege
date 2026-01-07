'''
InfHw24_6
https://education.yandex.ru/ege/inf/task/bdfb8f12-2b10-4f4b-99b0-6d2e045552e2
Текстовый файл состоит из заглавных букв латинского алфавита.
Определите последовательность наибольшей длины в прилагаемом файле, для которой выполняются два условия:
1) символы идут в алфавитном порядке,
2)в последовательности находится не более одной гласной (AEIOUY).
В ответе укажите длину найденной последовательности.
Пример:
Для строчки AEKZIOPSW ответ — число 4 (OPSW).
'''

f = open("InfHw24_6.txt")

from string import ascii_uppercase as ALPH

s = f.read()+"0"
# s = "AEKZIOPSW0"

M = 0
l = 0
r = 0
f1 = False

while r < len(s) - 1:
    if s[r+1] > s[r]:
        if s[r+1] in "AEIOUY" and not f1:
            f1 = True
            r += 1
        elif  not(s[r+1] in "AEIOUY"):
            r += 1
        else:
            # if M <= r - l + 1: print(r - l + 1, l, r, s[l:r+1])
            M = max(M, r - l + 1)
            l = r + 1
            r = l
    else:
        # if M <= r - l + 1: print(r - l + 1, l, r, s[l:r+1])
        M = max(M, r - l + 1)
        l = r + 1
        r = l

print(M)