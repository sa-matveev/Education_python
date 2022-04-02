'''
Выведите значение наименьшего нечетного элемента списка, гарантируется, что хотя бы один нечётный элемент в списке есть.

Формат ввода

Вводится список чисел. Все числа списка находятся на одной строке.

Формат вывода

Выведите ответ на задачу.

Тест 1
Входные данные:
0 1 2 3 4

Вывод программы:
1

Тест 2
Входные данные:
2 4 6 8 10 19
Вывод программы:
19

Тест 3
Входные данные:
5 4 3 2 1 0 -1 -2 -3 -4

Вывод программы:
-3
'''

print(
    min(
        filter(
            lambda x: x % 2 != 0,
            map(
                int,
                input().split()
            )
        )
    )
)
