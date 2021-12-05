"""
Справка:
    start - Из какого числа начинаются преобразования
    end - В какое число должны прийти преобразования
    not_occur - Какое число не должно встречаться в пути алгоритма
    occur - Какое число обязательно должно встречаться на пути алгоритма

Инструкции:
    x - Прибавить к текущему числу x
    y - Умножить текущее число на

"""
start = 3
finish = 35
not_occur = 17
occur = 12

x = 1
y = 2


def F(n, end):
    if n > end:
        return 0
    if n == end:
        return 1
    if n == not_occur:
        return 0
    return F(n+x, end) + F(n*y, end)


def main():
    print(F(start, occur) * F(occur, finish))


if __name__ == '__main__':
    main()
