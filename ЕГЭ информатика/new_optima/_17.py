def check_first(n, mini, maxix):
    quantity = 0
    summa_all = 0
    maxi = 0

    for value in range(mini, maxix):
        flag1, summa = first_condition(value, n)

        if flag1:
            print(value, summa)
            quantity += 1
            maxi = max(maxi, value)
            summa_all += value


def check_second(cc, x, z, occur):
    quantity = 0
    summa_all = 0
    maxi = 0

    for value in range(1937, 8593 + 1):
        flag2, new_value = second_condition(value, cc, x, z, occur)

        if flag2:
            print(value, new_value)
            quantity += 1
            maxi = max(maxi, value)
            summa_all += value


def first_condition(value, n):
    summa = 0

    for j in str(value):
        summa += int(j)

    if summa % n == 0:
        return True, summa
    else:
        return False, 0


def second_condition(value, cc, x, z, occur):
    new_value = ''

    while value > 0:
        new_value = str(value % cc) + new_value
        value = value // cc
    if occur:
        if int(new_value) % z == x:
            return True, new_value
        else:
            return False, 0
    else:
        if int(new_value) % z != x:
            return True, new_value
        else:
            return False, 0


def main():
    """
    Справка:
        Первое условие:
            n - число которому должна быть кратна сумма цифр числа

        Второе условие:
            сс - система счисления в которую надо перевести число для второго условия
            х - число которое должно быть на конце записи в СС (выше по справке)
            z - если (10 < x < 100) -> z=100; если (100 < x < 1000) -> z=1000 и так далее..
            occur - запись числа в сс заканчивается на x или НЕ заканчивается
    """
    # Сумма цифр числа кратна N
    n = 5

    # CC запись числа заканчивается / НЕ заканчивается на X
    cc = 16
    occur = True
    x = 78
    z = 100

    mini = 1171
    maxix = 8750 + 1

    quantity = 0
    maxi = 0
    summa_all = 0

    for value in range(mini, maxix):
        flag1, summa = first_condition(value, n)
        flag2, new_value = second_condition(value, cc, x, z, occur)

        if flag1 and flag2:
            print(value, new_value, summa)
            quantity += 1
            maxi = max(maxi, value)
            summa_all += value
    print()
    print("Всего чисел - ", quantity)
    print("Максимальное число - ", maxi)
    print("Сумма всех чисел - ", summa_all)
    #
    # print('----------------------------------------')
    # check_first(n, mini, maxix)
    # print('----------------------------------------')
    # check_second(cc, x, z, occur)


if __name__ == '__main__':
    main()
