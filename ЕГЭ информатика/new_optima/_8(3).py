"""
Программа для условия:
НЕ должна встречаться последовательность из n согласных/гласных букв

Справка:
    word - слово для преобразования
    quint - подсчёт количества подходящих комбинаций букв из слова
    n - количество первых букв попадающих под условие

    param['type'] - тип искомых букв(согласные/гласные)
"""

from itertools import permutations

alphabet_consonant = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м',
                      'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']

alphabet_vowel = ['у', 'е', 'э', 'о', 'а', 'ы', 'я', 'и', 'ю']

data = []

word = "осыпание"
quint = 0
n = 3

param = \
    {
        'type': 'vol',
    }

if param['type'] == 'vol':
    data = alphabet_vowel
elif param['type'] == 'cons':
    data = alphabet_consonant
print(data)

for i in permutations(word):
    cur = ''.join(i)
    flag = True
    x = 0
    lst = []
    for j in range(0, len(cur) - (n-1)):
        flag1 = 0

        for z in range(0, n):
            if cur[j + z] in data:
                flag1 += 1
        if flag1 == n:
            flag = False

    if flag:
        print(cur)
        quint += 1
print(quint)
