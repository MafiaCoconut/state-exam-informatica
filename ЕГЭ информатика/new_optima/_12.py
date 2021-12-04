def main():
    """
    p = искомое число
    x = 01 (4409)
    y = 04 (1019)
    z = 09 (1140)
    """

    p = 62

    x = 14
    y = 21
    z = 6

    for i1 in range(10):
        for i2 in range(10):
            for i3 in range(10):
                answer = i1 * x + i2 * y + i3 * z
                if answer == p:
                    print(answer, i1, i2, i3)


if __name__ == '__main__':
    main()
