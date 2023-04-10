import math


def main(m, a, n, x):
    final_sum = 0
    for i in range(1, n+1):
        for c in range(1, a+1):
            for j in range(1, m+1):
                final_sum += ((abs(j))**3+(math.atan(c)/10) + (i + x**2)**5)
    return final_sum


if __name__ == '__main__':
    m = 3
    a = 3
    n = 6
    x = -0.85
    print(main(m, a, n, x))
