import math


def main(z, x, y):
    n = 3
    final_sum = 0
    for i in range(1, n+1):
        final_sum += (z[n+1-(math.ceil(i/2))-1]**3
                      + x[i-1] + (y[math.ceil(i/3)-1])**2)
    return final_sum * 4


if __name__ == '__main__':
    z = [-0.49, 0.16, 0.7]
    x = [-0.08, -0.86, 0.01]
    y = [-0.8, 0.58, -0.23]
    print(main(z, x, y))
