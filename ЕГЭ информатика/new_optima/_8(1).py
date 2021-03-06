"""
Программа для подсчёта количества перестановок букв при условии
что какие-то буквы должны стоять на первых n местах
и какая-то часть совсем не должна встречаться!!!!!!!!!

Справка:
    word - слово для преобразования
    quint - подсчёт количества подходящих комбинаций букв из слова
    data - буквы которые должны стоять на первых n местах

    Требуется в строке 23 изменить "in" на "not in" в зависимости от условия
    not_occur - часть которая не должна встречаться в новой комбинации букв
    occur - часть которая должна встречаться в новой комбинации букв
"""

from itertools import permutations


def main():
    word = "безликость"
    quint = 0
    data = ['б', 'е', 'з']
    not_occur = 'ть'
    occur = ''

    for i in permutations(word):
        cur = ''.join(i)
        flag = 0
        # Менять not_occur и occur, а также (in) и (not in) в зависимости от условия!!!
        if not_occur not in cur:
            for j in range(len(data)):
                if cur[j] in data:
                    flag += 1
                if flag == len(data):
                    print(cur)
                    quint += 1
    print(quint)


if __name__ == '__main__':
    main()

