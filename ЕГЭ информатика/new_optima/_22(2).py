"""
НЕДОРАБОТАНО!!!!!!!!!!!!!!!!!!
"""

f = open("_22(2).txt", 'r')


def from_str_to_val(word):
    if word == 'A':
        return '6'
    elif word == 'B':
        return '5'
    elif word == 'C':
        return '4'
    elif word == 'D':
        return '3'
    elif word == 'E':
        return '2'
    elif word == 'F':
        return '1'


def from_val_to_str(word):

    if word == '6':
        return 'A'
    elif word == '5':
        return 'B'
    elif word == '4':
        return 'C'
    elif word == '3':
        return 'D'
    elif word == '2':
        return 'E'
    elif word == '1':
        return 'F'


def main():
    list1 = f.readline()
    list2 = list(list1)[:-1]
    print(list2)
    pos = from_str_to_val(list2[0])
    print(pos)
    max_pos = ''
    for i in range(1, len(list2)):
        x = from_str_to_val(list2[i])
        if x <= pos[-1]:
            pos += x
        elif x > pos[-1]:
            if len(max_pos) < len(pos):
                max_pos = pos
            pos = x
        else:
            pass

    answer = ''
    for i in range(len(max_pos)):
        answer += from_val_to_str(max_pos[i])
    print(answer)
    print(max_pos)


if __name__ == '__main__':
    main()
