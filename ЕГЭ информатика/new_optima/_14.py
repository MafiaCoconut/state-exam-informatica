"""
Справка:
    x - само выражение, где '^' заменено на '**'
    n - основание в котором написано выражение
"""


def main():
    x = 5 * 15**43 - 10 * 15**33 + 2 * 15**27 - 10*15**19 + 9*15**11
    i = x
    s = 0
    n = 15
    while i > 0:
        s += i % n
        i //= n
    print(s)


if __name__ == '__main__':
    main()