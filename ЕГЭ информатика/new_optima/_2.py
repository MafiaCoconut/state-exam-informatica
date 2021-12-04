"""
(a -> b)    =>   int(a <= b)
(a V b)     =>   (a or b)
(a & b)     =>   (a and b)
!a          =>   (not a)
a and a     =>   a
a V a       =>   a
a V (a & b) =>   a
a & (a V b) =>   a

Важно!!!
    использовать скобки на каждом действии
    a v (a & b) = a & b    =>   (a v (a & b)) = (a & b)


Пример:
    (b v a v (b -> c)) & ((a -> d) v c & c) & (!(a = e) v (!d -> (c = e)))
    int((b or a or int(b <= c)) and (int(a <= d) or c) and (not(a == e) or (int((not d) <= (c == e)))))

Место для заметок:
    e & (a & a v (b v a) = (b -> c) & (c -> d))
    e and (a or (b or a) == ((int(b <= c)) and int(c <= d)))
"""


def fifi(a, b, c, d, e):
    x = int(e and (((a and a) or (b or a)) == int((b <= c) and (c <= d))))
    if x == 1:

        print(a, b, c, d, e, '||', x)


for a in (0, 1):
    for b in (0, 1):
        for c in (0, 1):
            for d in (0, 1):
                for e in (0, 1):
                    fifi(a, b, c, d, e)
