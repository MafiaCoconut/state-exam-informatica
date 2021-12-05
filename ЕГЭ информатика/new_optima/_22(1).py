"""
ВНИМАНИЕ!!!!
Найдите триграммы, содержащие букву A.
Например, в ABCDABA это ABC, CDA, DAB, ABA.
В ответе укажите самую частую триграмму и
через пробел количество её вхождений в файл.
Если несколько триграмм встречаются одинаково
часто, укажите первую по алфавиту.
"""

trigram = ['AAA', 'AAB', 'AAC', 'AAD', 'AAE', 'AAF', 'ABA', 'ABB', 'ABC', 'ABD', 'ABE', 'ABF', 'ACA', 'ACB', 'ACC',
           'ACD', 'ACE', 'ACF', 'ADA', 'ADB', 'ADC', 'ADD', 'ADE', 'ADF', 'AEA', 'AEB', 'AEC', 'AED', 'AEE', 'AEF',
           'AFA', 'AFB', 'AFC', 'AFD', 'AFE', 'AFF', 'BAA', 'BAB', 'BAC', 'BAD', 'BAE', 'BAF', 'BBA', 'BCA', 'BDA',
           'BEA', 'BFA', 'CAA', 'CAB', 'CAC', 'CAD', 'CAE', 'CAF', 'CBA', 'CCA', 'CDA', 'CEA', 'CFA', 'DAA', 'DAB',
           'DAC', 'DAD', 'DAE', 'DAF', 'DBA', 'DCA', 'DDA', 'DEA', 'DFA', 'EAA', 'EAB', 'EAC', 'EAD', 'EAE', 'EAF',
           'EBA', 'ECA', 'EDA', 'EEA', 'EFA', 'FAA', 'FAB', 'FAC', 'FAD', 'FAE', 'FAF', 'FBA', 'FCA', 'FDA', 'FEA',
           'FFA']
trigram_count = [0] * 91

f = open("_22(1).txt", 'r')


def count_trigrams():
    # Считывание последовательности
    list1 = f.readline()
    list2 = list(list1)

    global trigram
    global trigram_count

    for i in range(len(list2) - 2):
        x = list2[i] + list2[i + 1] + list2[i + 2]
        for j in range(len(trigram)):
            if x == trigram[j]:
                trigram_count[j] += 1


def main():
    count_trigrams()

    print(trigram)
    print(trigram_count)

    lst3 = []
    for i in range(91):
        lst3.append([trigram_count[i], trigram[i]])
    lst3.sort()

    print(lst3[0], lst3[-1])


if __name__ == '__main__':
    main()
