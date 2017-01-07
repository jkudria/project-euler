#!/usr/bin/env python

# https://projecteuler.net/problem=14

# TODO: bruteforce takes much to long, but works (about 30 sec). Fix up.
# consider writing in C to check how much it takes then. Go to problem forum
# for some interesting optimizations.
# first optimization - check for powers of two at every iteration


def generate_collatz_length(num):
    """Generate a collatz sequence according to the rules given"""

    sequence = [num]
    while num != 1:
        if num % 2 == 0:
            num /= 2
        elif num % 2 == 1:
            num = num * 3 + 1
        sequence.append(num)

    return len(sequence)


def main():
    """Main entry point"""

    max_length = 0
    number = 0
    # only because all numbers below are mirrored on top with one or two more
    # added steps.
    for i in range(500001, 1000000):
        length = generate_collatz_length(i)
        if length > max_length:
            number = i
            max_length = length

    print(number)
    print(max_length)


if __name__ == '__main__':
    main()
