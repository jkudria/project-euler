#!/usr/bin/env python

from operator import mul
from functools import reduce


def main():
    num = '123456789'

    x = 0
    while len(num) <= 1_000_000:
        x += 1
        for i in range(10):
            num += (str(x) + str(i))

    indices = [0, 9, 99, 999, 9_999, 99_999, 999_999]

    print(reduce(mul, [int(num[index]) for index in indices]))


if __name__ == '__main__':
    main()
