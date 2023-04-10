class MealyError(Exception):
    pass


class Mealy:

    def __init__(self):
        self.state = 'A'

    def daub(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'C':
            self.state = 'D'
            return 2
        if self.state == 'D':
            self.state = 'B'
            return 5
        if self.state == 'F':
            self.state = 'G'
            return 7
        if self.state == 'G':
            self.state = 'E'
            return 9
        else:
            raise MealyError('daub')

    def slip(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'C':
            self.state = 'G'
            return 3
        if self.state == 'D':
            self.state = 'E'
            return 4
        if self.state == 'E':
            self.state = 'F'
            return 6
        if self.state == 'G':
            return 8
        else:
            raise MealyError('slip')


def test():
    o = main()
    cases = {'A': {'daub': 0, 'slip': MealyError},
             'B': {'daub': MealyError, 'slip': 1},
             'C': {'daub': 2, 'slip': 3},
             'D': {'daub': 5, 'slip': 4},
             'E': {'daub': MealyError, 'slip': 6},
             'F': {'daub': 7, 'slip': MealyError},
             'G': {'daub': 9, 'slip': 8}}
    try:  # Testing A-state
        o.slip()
    except MealyError:
        assert o.daub() == 0
    try:  # Testing B-state
        o.daub()
    except MealyError:
        assert o.slip() == 1
    assert o.daub() == 2
    assert o.daub() == 5
    assert o.slip() == 1
    assert o.daub() == 2
    assert o.slip() == 4
    try:
        o.daub()
    except MealyError:
        assert o.slip() == 6
    try:
        o.slip()
    except MealyError:
        assert o.daub() == 7
    assert o.slip() == 8
    assert o.slip() == 8
    assert o.daub() == 9
    assert o.slip() == 6
    assert o.daub() == 7
    assert o.slip() == 8
    assert o.slip() == 8

    o = main()
    try:  # Testing A-state
        o.slip()
    except MealyError:
        assert o.daub() == 0
    try:  # Testing B-state
        o.daub()
    except MealyError:
        assert o.slip() == 1
    assert o.daub() == 2
    assert o.daub() == 5
    assert o.slip() == 1
    assert o.slip() == 3
    assert o.daub() == 9
    try:
        o.daub()
    except MealyError:
        assert o.slip() == 6
    try:
        o.slip()
    except MealyError:
        assert o.daub() == 7
    assert o.slip() == 8
    assert o.slip() == 8
    assert o.daub() == 9
    assert o.slip() == 6
    assert o.daub() == 7
    assert o.slip() == 8
    assert o.slip() == 8


def main():
    return Mealy()


if __name__ == '__main__':
    test()
