import sys
import numpy as np


# Задание 1
def generate_groups():
    s1 = []
    s = ['И', 'Б', 'О']
    g = ['В', 'К', 'М', 'Н']
    groups0 = []
    groups1 = []
    groups2 = []
    groups = []
    for j in range(len(g)):
        s1 = s.copy()
        s.insert(1, g[j])
        s = "".join(s)
        groups0.append(s)
        s = s1.copy()
    i = 0
    for j in range(1, 125):
        if (i > 30):
            i = 0
        groups1 = groups0.copy()
        groups0[j % 4] += f'-{i + 1}'
        a = groups0[j % 4]
        i += 1
        groups2.append(a)
        groups0 = groups1.copy()
        groups2.sort()
    for i in range(18, 24):
        for k in groups2:
            k += f'-{i}'
            groups.append(k)
    print(groups)


print(generate_groups())


# Задание 2
def xuint(*args):
    sys.stdout.write(' '.join(map(str.upper, args)))


xuint('asd', 'sad')


# Задание 3
def decrypt(x, k):
    x0 = np.uint32(x[0])
    x1 = np.uint32(x[1])
    sum = np.uint32(0xC6EF3720)
    delta = np.uint32(0x9E3779B9)
    k0 = np.uint32(k[0])
    k1 = np.uint32(k[1])
    k2 = np.uint32(k[2])
    k3 = np.uint32(k[3])
    for i in range(32):
        x1 -= np.uint32(((x0 << 4) + k2) ^ (x0 + sum) ^ ((x0 >> 5) + k3))
        x0 -= np.uint32(((x1 << 4) + k0) ^ (x1 + sum) ^ ((x1 >> 5) + k1))
        sum -= np.uint32(delta)
    x[0] = np.uint32(x0)
    x[1] = np.uint32(x1)
    print('\n')
    print(hex(x[0]), hex(x[1]))


# Из условия задачи первые две буквы
x = [np.uint32(0xE3238557), np.uint32(0x6204A1F8)]
k = [np.uint32(0x0), np.uint32(0x4), np.uint32(0x5), np.uint32(0x1)]
decrypt(np.uint32(x), np.uint32(k))
