import math
import random


def task3_1():
    a = int(input("Input a:\n"))
    a += a
    a += a
    a += a + a
    print(a)


def task3_2():
    a = int(input("Input a:\n"))
    a += a
    a += a
    a += a
    a += a
    print(a)


def task3_3():
    x = int(input("Input x:\n"))
    y = x
    x += x
    x += x
    x += x
    y -= x
    y = x - y
    print(y)


# Task 3_4
def naive_mul(x, y):
    r = x
    for i in range(0, y - 1):
        x = x + r
    return x


# Task 3_5
def fast_mul(a, b):
    final_sum = 0
    starta = a
    startb = b
    print(a, b)
    while a > 0:
        print(a, b)
        divide = math.floor(a / 2)
        multb = math.floor(b * 2)
        if divide % 2 != 0:
            final_sum += multb
        a = math.floor(a / 2)
        b = math.floor(b * 2)
    if starta % 2 != 0:
        final_sum += startb
    assert final_sum == starta * startb
    print(f'Ответ: {final_sum}')


# Task 3_6
def fast_pow(a, b):
    final_sum = 0
    starta = a
    startb = a
    x = b
    b = a
    print(f'Start {a}, {b}')
    for i in range(x - 1):
        while a > 0:
            print(a, b, final_sum)
            divide = math.floor(a / 2)
            multb = math.floor(b * 2)
            if divide % 2 != 0:
                final_sum += multb
            a = math.floor(a / 2)
            b = math.floor(b * 2)
        if starta % 2 != 0:
            final_sum += startb
        print(f'From step: final_sum = {final_sum}, b = {startb}\n')
        a = final_sum
        final_sum = 0
        b = startb
    print(f'Ответ: {final_sum}')


# Task 3_7
def mul16(x, y):
    x1 = x & (2 ** 16 - 2 ** 8)
    x0 = x & (2 ** 8 - 1)
    y1 = y & (2 ** 16 - 2 ** 8)
    y0 = y & (2 ** 8 - 1)
    return x1 * y1 + x0 * y0 + x1 * y0 + x0 * y1


print(mul16(5689, 8941))


# Task 3_8
def mul16k(x, y):
    x1 = x & (2 ** 16 - 2 ** 8)
    x0 = x & (2 ** 8 - 1)
    y1 = y & (2 ** 16 - 2 ** 8)
    y0 = y & (2 ** 8 - 1)
    A1 = x1 * y1
    A2 = x0 * y0
    A3 = (x0 + x1) * (y0 + y1)
    return A1 + A2 + (A3 - A1 - A2)


print(mul16k(5689, 8941))


# Task 3_9
def fast_mul_gen(y):
    print(f'def f(x):')
    print(f'    r = x')
    for i in range(0, y - 1):
        print(f'    x = x + r')
    print('    return x')


# Task 3_10
def fast_mul_pow(y):
    print(f'def f(x):')
    print(f'    save_x = x')
    print(f'    r = x')
    for j in range(0, y - 1):
        print(f'    for i in range(0, save_x - 1):')
        print(f'        x = x + r')
        print(f'    r = x')
    print('    return x')


def f(x):
    save_x = x
    r = x
    for i in range(0, save_x - 1):
        x = x + r
    r = x
    for i in range(0, save_x - 1):
        x = x + r
    r = x
    return x


if __name__ == '__main__':
    # task3_5
    # fast_mul(random.randint(1, 100000), random.randint(1, 100000))
    # fast_mul_gen(3)
    # task3_3()
    fast_pow(12, 2)
    # print(mul16(61354, 59234))
    # fast_mul_pow(3)
    # print(f(int(input())))
    # print(naive_mul(2, 12))
