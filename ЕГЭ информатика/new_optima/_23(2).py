"""
Рассматриваются целые числа, принадлежащих числовому отрезку [start; end],
которые представляют собой произведение трёх различных простых делителей,
оканчивающихся на одну и ту же цифру

Инструкция:
1) запускаем
2) ждём пока val перестанет меняться
3) убераем комментарий
4) изменяем значение k на значение val в следствии пункта 2
5) запускаем и ждём
"""

def main():
    start = 318216
    end = 369453
    k = 274
    val = 0
    answer = []
    f = list(map(int, open('prime_numbers.txt', 'r').readline().split()))
    # print(*f)

    for i1 in f:
        for i2 in f:
            for i3 in f:
                if i1 != i2 != i3 != i1:
                    if i1 % 10 == i2 % 10 == i3 % 10 == i1 % 10:
                        # print(i1, i2, i3)
                        x = i1 * i2 * i3
                        if start <= x <= end:
                            if x not in answer:
                                val += 1
                                answer.append(x)
                                print(val, x, i1, i2, i3)
                        # if val == k:
                        #     answer.sort()
                        #     print(answer)
                        #     exit()


if __name__ == '__main__':
    main()
