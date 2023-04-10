from struct import *

FMT = dict(
    char='<c',
    int8='<b',
    uint8='<B',
    int16='<h',
    uint16='<H',
    int32='<i',
    uint32='<I',
    int64='<q',
    uint64='<Q',
    float='<f',
    double='<d'
)


def parse(buf, offs, ty):
    return unpack_from(FMT[ty], buf, offs)[0], offs + calcsize(FMT[ty])


def parse_a(buf, offs):
    a1_size = 3
    a1 = ''
    for _ in range(a1_size):
        val, offs = parse(buf, offs, 'char')
        a1 += str(val)[2]
    a2, offs = parse(buf, offs, 'uint32')
    a3, offs = parse_b(buf, offs)
    return dict(A1=a1, A2=a2, A3=a3), offs


def parse_b(buf, offs):
    b1, offs = parse(buf, offs, 'double')
    b2, offs = parse_c(buf, offs)
    b3, offs = parse(buf, offs, 'int8')

    b4_size, offs = parse(buf, offs, 'uint32')
    b4_offs, offs = parse(buf, offs, 'uint16')
    b4 = []
    for _ in range(b4_size):
        val, b4_offs = parse_d(buf, b4_offs)
        b4.append(val)

    b5, offs = parse(buf, offs, 'double')

    b6_size, offs = parse(buf, offs, 'uint32')
    b6_offs, offs = parse(buf, offs, 'uint32')
    b6 = []
    for _ in range(b6_size):
        val, b6_offs = parse(buf, b6_offs, 'int8')
        b6.append(val)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, 'float')
    c2, offs = parse(buf, offs, 'int16')
    return dict(C1=c1, C2=c2), offs


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'double')

    d2_size, offs = parse(buf, offs, 'uint16')
    d2_offs, offs = parse(buf, offs, 'uint16')
    d2 = []
    for _ in range(d2_size):
        val, d2_offs = parse(buf, d2_offs, 'int8')
        d2.append(val)
    d3, offs = parse(buf, offs, 'uint16')
    return dict(D1=d1, D2=d2, D3=d3), offs


def main(buf):
    return parse_a(buf, 4)[0]
