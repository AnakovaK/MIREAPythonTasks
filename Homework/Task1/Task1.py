import math


def main(z, x, y):
    left_up = (math.log10(z - ((x**3)/66) - (y**2)))**3 + (52*y)
    down_left = 94*((math.exp((z**3)/5+21*y))**6)+((math.floor(x))**2)/41
    right_up = 67*math.exp(20+x**2+57*y) - (math.tan(z**3+y**2+95*x))**4
    right_down = (y - z**2 - 95*(z**3))**7 + 10*((57*x-x**2)**3)
    return (left_up/down_left) - (right_up/right_down)


if __name__ == '__main__':
    z = 0.7
    x = 0.69
    y = -0.11
    print(main(z, x, y))
