"""
Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.

Формат ввода

Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с названия страны, затем идут названия городов этой страны. Название каждого город состоит из одного слова. В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.

Формат вывода

Для каждого из запроса выведите название страны, в котором находится данный город.

Тест 1
Входные данные:
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa
3
Odessa
Moscow
Novgorod

Вывод программы:
Ukraine
Russia
Russia

Тест 2
Входные данные:
5
A B
C D
E F
G H
I J
5
J
H
F
D
B

Вывод программы:
I
G
E
C
A

Тест 3
Входные данные:
5
A B
C D E
F G H I
J K L M N
O P Q R S T
15
T
S
N
R
M
I
Q
L
H
E
P
K
G
D
B

Вывод программы:
O
O
J
O
J
F
O
J
F
C
O
J
F
C
A
"""


file = open("input.txt", "r", encoding="utf-8-sig")
i = int(file.readline())
countries_dict = {}

for k, line in enumerate(file, start=1):
    if k > i:
        i = int(line)
        break
    else:
        line = line.split()
        for index, word in enumerate(line):
            if index == 0:
                country = word
            else:
                countries_dict[word] = country

for z, line in enumerate(file, start=1):
    if z > i:
        break
    else:
        line = line.strip("\n")
        print(countries_dict[line])

file.close()