'''
В выборах Президента Российской Федерации побеждает кандидат, набравший свыше половины числа голосов избирателей.
Если такого кандидата нет, то во второй тур выборов выходят два кандидата, набравших наибольшее число голосов.

Формат ввода

Каждая строка входного файла содержит имя кандидата, за которого отдал голос один избиратель.
Известно, что общее число кандидатов не превосходит 20, но в отличии от предыдущих задач список кандидатов явно не задан.
Читайте данные из файла input.txt с указанием кодировки utf8.

Формат вывода

Если есть кандидат, набравший более 50% голосов, программа должна вывести его имя.
Если такого кандидата нет, программа должна вывести имя кандидата, занявшего первое место,
затем имя кандидата, занявшего второе место. Выводите данные в файл output.txt с указанием кодировки utf8.

Тест 1
Входные данные:
Полуэкт Варфоломеев
Варфоломей Полуэктов
Полуэкт Варфоломеев

Вывод программы:
Полуэкт Варфоломеев

Тест 2
Входные данные:
Полуэкт Варфоломеев
Варфоломей Виссарионов
Виссарион Полуэктов
Варфоломей Виссарионов
Варфоломей Виссарионов
Полуэкт Варфоломеев

Вывод программы:
Варфоломей Виссарионов
Полуэкт Варфоломеев
'''

file = open("input.txt", encoding="utf-8-sig")
output_file = open("output.txt", "w", encoding="utf8")

dict_cadidats = dict()
list_candidats = list()
summ_voices = 0

for name in file:
    name = name.strip("\n")
    if name in dict_cadidats:
        dict_cadidats[name] = int(dict_cadidats.get(name)) + 1
        summ_voices += 1
    else:
        dict_cadidats[name] = 1
        summ_voices += 1

for candidat in dict_cadidats.items():
    list_candidats.append((candidat[1], candidat[0]))
list_candidats = sorted(list_candidats, reverse=True)

if list_candidats[0][0] > summ_voices / 2:
    print(list_candidats[0][1], file=output_file)
else:
    print(list_candidats[0][1], file=output_file)
    print(list_candidats[1][1], file=output_file)

file.close()
output_file.close()
