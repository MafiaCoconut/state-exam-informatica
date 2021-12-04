"""
Справка:
    x - значение которое должна выводить программа
    z - из скольки знаков состоят числа
    n - сколько чисел нужно добавить в сумму
    t = 1 - нужно найти максимальное
    t = 2 - нужно найти минимальное
"""

x = 9
z = 4
n = 5
t = 2
data = []
summa = 0

for i in range(10**(z-1), 10**z):
    N, S = i, 1

    # Сюда подстовляется программа из варианта
    while N > 0:
        S = S * (N % 10)
        N //= 10

    if S == x:
        data.append(i)

print(data)

if t == 1:
    for i in range(len(data)-1, len(data) - 1 - n, -1):
        summa += data[i]
elif t == 2:
    for i in range(n):
        summa += data[i]
print(summa)
