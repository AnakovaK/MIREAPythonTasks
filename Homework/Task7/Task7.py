def main(number):
    number = int(number)
    N1 = 0b0000000000000000000000011
    N2 = 0b0000000000000000011111100
    N3 = 0b0000000011111111100000000
    N4 = 0b0000111100000000000000000
    N5 = 0b1111000000000000000000000

    trynumber = (int(number))
    N1solve = N1 & trynumber
    N1 = N1 & trynumber
    N2solve = N2 & trynumber
    N2 = N2solve >> 2
    N3solve = N3 & trynumber
    N3 = N3solve >> 8
    N4solve = N4 & trynumber
    N4 = N4solve >> 17
    N5solve = N5 & trynumber
    N5 = N5solve >> 21
    '''print("N1: ", N1)
    print("N2: ", N2)
    print("N3: ", N3)
    print("N4: ", N4)
    print("N5: ", N5)'''
    return str(N1), str(N2), str(N3), str(N4), str(N5)


if __name__ == '__main__':
    x = '5018591'
    main(x)
