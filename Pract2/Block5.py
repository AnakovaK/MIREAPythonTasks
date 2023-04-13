'''
ham_dist(0b10, 0b11)
1
ham_dist(0b1100, 0b0011)
4'''

# Задача 1

# В лоб
import binascii


def ham_dist(x, y):
    binx = str(bin(x))
    binx = binx[2:len(str(binx))]
    biny = str(bin(y))
    biny = biny[2:len(str(biny))]
    if len(binx) < len(biny):
        for i in range(len(biny) - len(binx)):
            binx = '0' + binx
    if len(binx) > len(biny):
        for i in range(len(binx) - len(biny)):
            biny = '0' + biny
    start_count = 0
    for i in range(len(binx)):
        if binx[i] != biny[i]:
            start_count += 1
    return start_count


def izyashno(x, y):
    pass


# print(ham_dist(0b11011, 0b00011))


# Задание 2
def convert_to_1_or_0(x):
    to_check = x
    if str(to_check).count('1') > str(to_check).count('0'):
        return '1'
    else:
        return '0'


text = [815608, 2064837, 2093080, 2063879, 196608, 2067983, 10457031, 1830912, 2067455, 2093116, 1044928, 2064407,
        6262776, 2027968, 4423680, 2068231, 2068474, 1999352, 1019903, 2093113, 2068439, 2064455, 1831360, 1936903,
        2067967, 2068456]
answer = []
for i in range(len(text)):
    text[i] = bin(text[i])
for i in range(len(text)):
    text[i] = text[i][2:]
for i in range(len(text)):
    if len(text[i]) % 3 != 0:
        while len(text[i]) % 3 != 0:
            text[i] = '0' + text[i]
for i in range(len(text)):
    temp_number = ''
    for j in range(0, 21, 3):
        temp_number += convert_to_1_or_0(str(text[i][j:j + 3]))
    answer.append(temp_number)
# print(text)
# print(answer)
for i in range(len(text)):
    n = int(answer[i], 2)
    # print(binascii.unhexlify('%x' % n))
# ANSWER:    Very@i6porta7tinformation


# Задание 3
from functools import cache


@cache
def lev_dist(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


# print(lev_dist('слон', 'столб'))

# Задание 4 и 5
@cache
def lev_dist_ops(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
            if min(add, delete, change) == add:
                print("Добавление")
            elif min(add, delete, change) == delete:
                print("Удаление")
            if min(add, delete, change) == change:
                print("Замена")
    return current_row[n]


print(lev_dist_ops('слон', 'столб'))
