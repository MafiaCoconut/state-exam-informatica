from itertools import permutations

word = ""
alphabit_val = ['а', 'у', 'е', 'ё', 'э', 'о', 'ы', 'я', 'и', 'ю']
count = 0

for i in permutations(word):
    cur = ''.join(i)
    

print(count)
