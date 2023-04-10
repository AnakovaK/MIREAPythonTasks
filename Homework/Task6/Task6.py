def RHTML_route(array):
    if array[2] == 'D':
        if array[1] == 1984:
            return 0
        elif array[1] == 1985:
            return 1
        else:
            return 2
    else:
        if array[0] == 2004:
            return 3
        elif array[0] == 2002:
            return 4
        else:
            return 5


def REXX_route(array):
    if array[1] == 1984:
        return 6
    elif array[1] == 1985:
        return 7
    else:
        if array[0] == 2004:
            return 8
        elif array[0] == 2002:
            return 9
        else:
            return 10


def main(array):
    if array[3] == 'RHTML':
        return RHTML_route(array)
    else:
        return REXX_route(array)


if __name__ == '__main__':
    x = [2002, 2011, 'D', 'REXX']
    print(main(x))
