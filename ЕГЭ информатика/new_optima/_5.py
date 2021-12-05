def work1(val):
    val = str(val)
    if val.count('1') % 2 == 0:
        val += '0'
    else:
        val += "1"
    if val.count('1') % 2 == 0:
        val += '0'
    else:
        val += "1"
    return val


def work2(val):
    val = str(val)
    if val.count('1') % 2 == 0:
        val += '1'
    else:
        val += "0"
    val += str(val.count('1') % 2)
    return val


def main():
    """
    Справка:
        val - число которое дано по условию
        val_bin - двоичное число val

        or_r - укороченная часть var_bin для долнейшей модификации
        r - нормальное число or_r
    Условие:
        Если в числе 100001 -> 1000010 || используем work1
        Если в числе 100000 -> 1000000 || используем work2
    """
    val = 96
    val_bin = bin(val)[2:]

    or_r = val_bin[:-2]
    r = int(or_r, 2)
    print(val, val_bin)
    print(r, or_r, sep='  ')

    for i in range(r, 100):

        # ЗДЕСЬ МЕНЯТЬ work1 И work2
        x = work1(bin(i)[2:])

        if int(x, 2) > val:
            print("После алгоритма - ", x)
            print("Какое число получилось после алгоритма (R) - ", int(x, 2))
            print("Из какого числа получилось новое число (N) - ", i)
            break


if __name__ == '__main__':
    main()
