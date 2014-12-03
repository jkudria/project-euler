#!/usr/bin/env python

import operator
import functools


def append_line_to_numbers(num_list, line_string):
    for num in line_string:
        if num != '\n':
            num_list.append(int(num))

    return num_list


def main():
    thousand_numbers = []
    current_thirteen = []
    sums = []  # later we'll take the largest from here

    # parsing all of the lines of numbers into the thousand_numbers list
    with open('8.txt', 'r') as numbers_file:
        for line in numbers_file:
            thousand_numbers = append_line_to_numbers(thousand_numbers, line)

    while len(thousand_numbers) > 12:
        # taking the first 13 numbers from the thousand_numbers list
        current_thirteen = thousand_numbers[:13]

        # removing the first element of the thousand_numbers list so that we can
        # always do thousand_numbers[:13] to get the next 13 numbers
        thousand_numbers = thousand_numbers[1:]

        # if there is a 0 in the list, the whole product will be 0, so no point
        if 0 not in current_thirteen:
           sums.append(functools.reduce(operator.mul, current_thirteen, 1))

    print(max(sums))

if __name__ == '__main__':
    main()
