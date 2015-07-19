#!/usr/bin/env python

# https://projecteuler.net/problem=14

# TODO: bruteforce takes much to long


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
    for i in range(1, 1000000):
        print(i)
        length = generate_collatz_length(i)
        if length > max_length:
            max_length = length

    print(max_length)


if __name__ == '__main__':
    main()
