x = 0
i = x
s = 0
n = 0
while i > 0:
    s += i % n
    i //= n
print(s)
