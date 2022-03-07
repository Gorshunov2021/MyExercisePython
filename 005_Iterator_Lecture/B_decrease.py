# класс объектов, которые одновременно являюстся и
# итерируемыми (есть метод __iter__),
# и итераторами (есть метод __next__);
# преимущества:
# 1. один класс вместо двух - меньше писать и выдумывать названий
# 2. одно общее состояние - не надо передавать переменные
class RangeIterableIterator:
    def __init__(self, size):
        self.x = size

    # раз сам себе итератор - сам себя и возвращает


def __iter__(self):
    return self


def __next__(self):
    self.x -= 1
    if self.x <= 0:
        raise StopIteration
    return '#' * self.x