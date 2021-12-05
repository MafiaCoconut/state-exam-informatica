"""
Найдите числа, все нетривиальные делители которых образуют
арифметическую прогрессию с шагом n на интервале [start; end].
Для каждого найденного числа выведите само число и
наименьший из нетривиальных делителей.
"""


f = list(map(int, open('prime_numbers.txt', 'r').readline().split()))
start = 15000000
end = 16000000
n = 8
answer = []
lst = []

for i in range(len(f)):
    for j in range(i + 1, len(f) - 1):
        if f[i] + n == f[j]:
            x = f[i] * f[j]
            if start <= x <= end:
                print(x, f[i], f[j])
