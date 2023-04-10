def main(s):
    s = s.replace('<<', '')
    s = s.replace('>>', '')
    s = s.replace(' ', '')
    s = s.replace('.', '')
    s = s.replace('\n', '')
    s = s.split(',')
    dict = {}
    s = s[:-1]
    length = len(s)
    for i in range(len(s)):
        s[i] = s[i][4:]
        s[i] = s[i].split('is#')
    for i in range(length):
        dict[f'{s[i][0]}'] = int(s[i][1])
    return dict


if __name__ == '__main__':
    s = ''
    main(s)
