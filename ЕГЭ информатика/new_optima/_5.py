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
        Если в числе   четное количество 1, то добавляем 0, и наоборот  || используем work1
        Если в числе нечетное количество 1, то добавляем 0, и наоборот  || используем work2
    """
    val = 130
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
