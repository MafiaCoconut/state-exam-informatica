"""
Если в условии НЕ ДАНО количество страниц всего

Справка:
    I - всего занимает объёма
    x - во сколько страниц с текстом больше чем страниц с изображением

    kt - сколько текста на одной странице
    it - кодировка текста (бит)
    It - занимает объём текст

    ki - размер картинки на одной странице
    ii - коидровка картинки(N=256 -> ii = 8)
    Ii - занимает объём картинка

    pg_i = сколько страниц изображений
    pg_t = сколько страниц текста

    Если страниц с текстом в 16 раз больше чем страниц с изображением:
    pg_t = 16 * pg_i
    Если срашивают сколько страниц всего, то ответ pg_t + pg_i
"""


def main():
    I = 5 * 2 ** 23
    x = 16

    kt = 32 * 64
    it = 8
    It = kt * it

    ki = 512 * 256
    ii = 8
    Ii = ki * ii

    print(' I =', I)
    print('It =', It)
    print('Ii =', Ii)
    print()

    pg_i = I // (It * x + Ii)
    pg_t = pg_i * x
    pg = pg_t + pg_i

    print('pg_t =', pg_t)
    print('pg_i =', pg_i)
    print('  pg =', pg)


if __name__ == '__main__':
    main()
