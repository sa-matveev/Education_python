'''
По данному числу N выведите все перестановки чисел от 1 до N в лексикографическом порядке.

Формат ввода

Задано 1 число: N (0<N<10).

Формат вывода

Необходимо вывести все перестановки чисел от 1 до N в лексикографическом порядке.
Перестановки выводятся по одной в строке, числа в перестановке выводятся без пробелов.

Тест 1
Входные данные:
1

Вывод программы:
1

Тест 2
Входные данные:
2

Вывод программы:
12
21

Тест 3
Входные данные:
3

Вывод программы:
123
132
213
231
312
321
'''

import itertools as it

print(
    *map(
        "".join,
        it.permutations(
            map(
                str,
                range(1, int(input()) + 1)
            )
        )
    ),
    sep="\n"
)
