'''
Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
Слова должны быть отсортированы по убыванию их количества появления в тексте,
а при одинаковой частоте появления — в лексикографическом порядке.

Указание.

После того, как вы создадите словарь всех слов, вам захочется отсортировать его по частоте встречаемости слова.
Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов:
частота встречаемости слова и само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')].
Тогда стандартная сортировка будет сортировать список кортежей, при этом кортежи сравниваются по первому элементу,
а если они равны —то по второму. Это почти то, что требуется в задаче.

Формат ввода

Вводится текст.

Формат вывода

Выведите ответ на задачу.

Тест 1
Входные данные:
hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme

Вывод программы:
damme
is
name
van
bond
claude
hi
my
james
jean
what
your

Тест 2
Входные данные:
oh you touch my tralala
mmm my ding ding dong

Вывод программы:
ding
my
dong
mmm
oh
touch
tralala
you

Тест 3
Входные данные:
ai ai ai ai ai ai ai ai ai ai

Вывод программы:
ai
'''

file = open("input.txt", encoding="utf-8-sig")
dictionary = dict()
list_of_tuple = list()

for line in file:
    for word in line.split():
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] = int(dictionary.get(word)) + 1

for key, value in dictionary.items():
    list_of_tuple.append([-value, key])

for item in sorted(list_of_tuple):
    print(item[1])

file.close()
