"""
Добавьте в предыдущий класс следующие методы:

 __add__, принимающий вторую матрицу того же размера и возвращающий сумму матриц.

 __mul__, принимающий число типа int или float и возвращающий матрицу, умноженную на скаляр.

 __rmul__, делающий то же самое, что и __mul__. Этот метод будет вызван в том случае, аргумент находится справа. Для реализации этого метода в коде класса достаточно написать __rmul__ = __mul__.

Иллюстрация:

 В следующем случае вызовется __mul__: Matrix([[0, 1], [1, 0]) * 10.

 В следующем случае вызовется __rmul__ (так как у int не определен __mul__ для матрицы справа): 10 * Matrix([[0, 1], [1, 0]).

Разумеется, данные методы не должны менять содержимое матрицы.

Формат ввода

Как в предыдущей задаче.

Формат вывода

Как в предыдущей задаче.

# Task 2 check 1
m = Matrix([[10, 10], [0, 0], [1, 1]])
print(m.size())

Вывод программы:
(3, 2)

Тест 2
Входные данные:
# Task 2 check 2
m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)

Вывод программы:
1	1	0
20	1	-1
-1	-2	1

Тест 3
Входные данные:
# Task 2 check 3
m = Matrix([[1, 1, 0], [0, 2, 10], [10, 15, 30]])
alpha = 15
print(m * alpha)
print(alpha * m)

Вывод программы:
15	15	0
0	30	150
150	225	450
15	15	0
0	30	150
150	225	450
"""

from sys import stdin
import copy


class Matrix(list):
    def __init__(self, old_list):
        self.save_list = copy.deepcopy(old_list)

    def __str__(self):
        new_str = str()
        for i, one_list in enumerate(self.save_list, start=1):
            for k, num in enumerate(one_list, start=1):
                if k < len(one_list):
                    new_str += str(num) + "\t"
                else:  # k == len
                    new_str += str(num)
            if i < len(self.save_list):
                new_str += "\n"
        return new_str

    def size(self):
        return len(self.save_list), len(self.save_list[0])

    def __add__(self, other):
        add_matrix = list()
        temp_list = list()
        for i, get_list in enumerate(self.save_list):
            for k, get_num in enumerate(get_list):
                if k < (len(get_list) - 1):
                    temp_list.append(get_num + other.save_list[i][k])
                else:
                    temp_list.append(get_num + other.save_list[i][k])
                    add_matrix.extend([temp_list])
                    temp_list = list()
        return Matrix(add_matrix)

    def __mul__(self, other):
        temp_list = list()
        mul_list = list()
        for i, get_list in enumerate(self.save_list):
            for k, num in enumerate(get_list):
                if k < (len(get_list) - 1):
                    num *= other
                    temp_list.append(num)
                else:
                    num *= other
                    temp_list.append(num)
                    mul_list.extend([temp_list])
                    temp_list = list()
        return Matrix(mul_list)

    __rmul__ = __mul__


exec(stdin.read())
