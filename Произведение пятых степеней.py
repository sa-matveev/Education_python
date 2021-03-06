'''
На вход подаётся последовательность натуральных чисел длины n≤1000.
Посчитайте произведение пятых степеней чисел в последовательности.

Формат ввода

Вводится последовательность чисел

Формат вывода

Выведите ответ на задачу

Тест 1
Входные данные:
1 1 1 2

Вывод программы:
32

Тест 2
Входные данные:
2 1 1 2 2

Вывод программы:
32768

Тест 3
Входные данные:
10 100 1000 10000 2

Вывод программы:
3200000000000000000000000000000000000000000000000000

'''

import functools as ft

print(
    ft.reduce(
        lambda x, y: x * y,
        map(
            lambda x: x**5,
            map(
                int, input().split()
            )
        )
    )
)


