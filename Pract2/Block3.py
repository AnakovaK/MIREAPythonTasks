def t1():
    return list(map(float, input()))


def t2():
    return len(set(input().split()))


def t3():
    return input()[::-1]


def t4():
    return [i for i, val in enumerate(input()) if val == '']


def t5():
    return sum(input()[::2])


def t6():
    return max(input(), key=len)


##t7
# t7 = lambda n = int(input()): n % sum(int(d) for d in str(n)) == 0


def t8():
    import string, random

    return (''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(5)))


def t9(s):
    import itertools

    return ''.join(str(len(list(group))) + key for key, group in itertools.groupby(s))
