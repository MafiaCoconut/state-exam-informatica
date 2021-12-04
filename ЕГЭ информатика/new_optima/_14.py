def check(val):
    data = ['A', 'B', 'C', 'D', 'E', 'F']
    return data[val % 10]


def get_zeros(number_of_zero, numbers, signs):
    z = -1
    for i in range(0, len(number_of_zero)):
        word = ''
        for j in range(int(number_of_zero[i])):
            word += '0'
        if i == 0:
            word = str(numbers[0]) + word
        else:
            z += 1
            word = signs[z] + str(numbers[i]) + word
        word1 = word.rjust(int(number_of_zero[0]) + 1, ' ')
        print(word1)


"""
Справка:
    equation - уравнение где везе нужно поставить пробелы
    cc - система счисления
"""


def main():
    # equation = '2 * 13 ^ 43 - 12 * 13 ^ 32 + 13 ^ 25 - 2 * 13 ^ 17 + 13 ^ 11'
    # equation = '4 * 14 ^ 43 - 2 * 14 ^ 32 + 6 * 14 ^ 25 - 8 * 14 ^ 17 + 9 * 14 ^ 9'
    equation = ' 8 * 11 ^ 43 - 11 ^ 35 + 2 * 11 ^ 27 - 11 ^ 16 + 10 * 11 ^ 11'
    cc = str(11)
    y = equation.split(' ')

    number_of_zero = []
    numbers = []
    signs = []
    for i in range(len(y)):
        z = 0
        if y[i] == '^':
            number_of_zero.append(y[i + 1])
        if y[i] == '+' or y[i] == '-':
            signs.append(y[i])

        if y[i] == cc and y[i - 1] != '^':
            if y[i - 1] != '*':
                z = 1
            else:
                z = int(y[i - 2])
            if z >= 10:
                z = check(z)
            numbers.append(z)
    print(number_of_zero)
    print(numbers)
    print(signs)
    get_zeros(number_of_zero, numbers, signs)


if __name__ == '__main__':
    main()

