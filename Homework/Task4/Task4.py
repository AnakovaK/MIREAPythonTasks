import math


def main(n):
    if n == 0:
        return 0.42
    elif n == 1:
        return -0.26
    elif n >= 2:
        return 1 + 81*((math.cos(main(n-2)))**3) + main(n-1)


if __name__ == '__main__':
    n = 5
    print(main(n))
