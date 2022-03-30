'''
Во входном файле (вы можете читать данные из файла input.txt) записан текст.
Словом считается последовательность непробельных подряд идущих символов.
Слова разделены одним или большим числом пробелов или символами конца строки.
Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
Формат ввода
Вводится текст.
Формат вывода
Выведите ответ на задачу.

Тест 1
Входные данные:
one two one tho three

Вывод программы:
0 0 1 0 0

Тест 2
Входные данные:
She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.

Вывод программы:
0 0 0 0 0 0 1 0 0 1 0 0 1 0 2 2 0 0 0 0 1 2 3 3 1 1 4 0 1 0 1 2 4 1 5 0 0

Тест 3
Входные данные:
aba aba; aba @?"

Вывод программы:
0 0 1 0
'''

file = open("input.txt", "r", encoding="utf-8-sig")

answer_dict = {}

for line in file:
    line = line.split()
    for word in line:
        if answer_dict.setdefault(word) is None:
            print(0, end=" ")
            answer_dict[word] = 1
        else:
            print(answer_dict.get(word), end=" ")
            answer_dict[word] = answer_dict.get(word) + 1
file.close()
