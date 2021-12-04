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
end = 33
not_occur = 16
occur = 6

x = 1
y = 2


def F(n):
    if n > end:
        return 0
    if n == end:
        return 1
    if n == not_occur:
        return 0
    return F(n+x) + (0 if (n < occur < y * n) else F(n * y))


def main():
    print(F(start))


if __name__ == '__main__':
    main()
