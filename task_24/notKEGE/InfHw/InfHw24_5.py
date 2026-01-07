'''
InfHw24_5
https://education.yandex.ru/ege/inf/task/01dfb7d5-1b71-470d-adf4-612e4adaaf7e
Текстовый файл состоит из символов латинского алфавита в нижнем регистре (a—z) и цифр (0-9).
Определите в прилагаемом файле максимальную длину подстроки (непрерывной подпоследовательности), которая состоит из повторяющегося слова "yandex". Последнее слово в цепочке может быть неполным. По правилам leet (1337) символ "a" может быть заменён на символ "4", а символ "e" — на символ "3".
Так, в строке "qyandqqyand3xy4q" есть две подходящие подстроки: "yand" и "yand3xy4".
'''


a = "yandexyandexyandexyandexyandexyandexyandexyandexyandexyandexyandexyandexyandexyandexyandex"
print(len(a))