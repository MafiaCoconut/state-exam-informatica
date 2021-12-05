"""
Пусть M(N) - произведение t наименьших различных натуральных
делителей натурального числа N, не считая единицы.
Найдите k наименьших натуральных чисел, превышающих start, для которых

"""


def main():
    start = 200000000
    t = 7
    k = 5
    answer = []

    for i in range(start + 1, start + 50):
        x = i
        lst = []
        for j in range(2, 1000):
            if x % j == 0:
                lst.append(j)
                if len(lst) == t:
                    break

        if len(lst) == t:
            l = 1
            for j in range(t):
                l *= lst[j]
            if l < i:
                print(i, l, lst)
                answer.append(l)
    print(*answer[:k])

if __name__ == '__main__':
    main()
