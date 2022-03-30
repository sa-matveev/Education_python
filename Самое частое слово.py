"""
Дан текст. Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

Формат ввода

Вводится текст.

Формат вывода

Выведите ответ на задачу.

Тест 1
Входные данные:
apple orange banana banana orange

Вывод программы:
banana

Тест 2
Входные данные:
oh you touch my tralala mmm my ding ding dong

Вывод программы:
ding

Тест 3
Входные данные:
q w e r t y u i o p
a s d f g h j k l
z x c v b n m

Вывод программы:
a
"""

file = open("input.txt", encoding="utf-8-sig")
dictionary = {}

for line in file:
    line = line.split()
    for word in line:
        if dictionary.get(word) is None:
            dictionary[word] = 1
        else:
            dictionary[word] = int(dictionary.get(word)) + 1

print(max(sorted(dictionary), key=dictionary.get))

file.close()
