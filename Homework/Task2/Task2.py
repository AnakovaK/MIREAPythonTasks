import math


def main(x):
    if x < -15:
        return 51 * x ** 2 + 54 * ((1 - (x ** 2) / 31 - 93 * (x ** 3)) ** 7) \
               + (math.exp(1 - x / 88)) ** 3
    elif -15 <= x < 69:
        return x ** 2 + 11 * ((abs(x)) ** 6) + ((94 * (x ** 2)) ** 5)
    elif 69 <= x < 143:
        return x ** 5 - (56 * x) ** 3 - 8 * (0.03 + 85 * x ** 2 + x ** 3)
    elif x >= 143:
        return 72 + x ** 3 + (math.atan(x)) ** 2


if __name__ == '__main__':
    x = 95
    print(main(x))
