x = 5 * 15**43 - 10 * 15**33 + 2 * 15**27 - 10*15**19 + 9*15**11
i = x
s = 0
n = 15
while i > 0:
    s += i % n
    i //= n
print(s)
