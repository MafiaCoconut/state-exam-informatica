"""
Найдите подпоследовательность подряд идущих букв,
которые при этом расположены по неубыванию с точки
зрения алфавитного порядка.
Например, в ABCABAC это последовательности
A, B, C, A, B, A, AB, ABC, BC, AB, AC.
"""


def main():
    f = list(map(str, open("_22(2).txt", 'r').readline()))
    flag = False
    answer = []
    x = []

    for i in range(len(f)):
        if not flag:
            if f[i] == 'A':
                flag = True
                x.append(f[i])
        else:
            y = ord(f[i])
            z = ord(x[-1])
            if z <= y:
                x.append(f[i])
            else:

                if len(x) > len(answer):
                    answer = x
                x = []
                flag = False
    for i in answer:
        print(i, end='')


if __name__ == '__main__':
    main()
