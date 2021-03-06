"""
Справка:
    I - Объём информации          || Мегабайты
    x - Количество каналов записи || ...
    f - Частота дискритизации     || Килогерцы
    i - разрешение                || биты
    t - количество минут          || минуты
"""


def main():
    I = 3750 * 2 ** 23
    x = 4
    f = 64 * 1000
    i = 8

    t = I / (x * f * i * 60)

    print("Количество минут: ", t)
    print("(x * f * i * t * 60) = ", x * f * i * t * 60)
    print("                   I = ", I)


if __name__ == '__main__':
    main()
