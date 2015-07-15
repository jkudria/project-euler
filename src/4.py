#!/usr/bin/env python

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(number):
    """Check if given number is a palindrome."""

    number = str(number)

    return number == number[::-1]


def main():
    """Main entry point"""

    # brute force solution
    # testing only 900-100 beacuse I'm sure there's a palindrome multiple in
    # there, and if so it'll be larger than any other 3x3 digit palindrome
    # multiples

    max = 0
    for a in range(900, 1000):
        for b in range(900, 1000):
            if is_palindrome(a*b) and a*b > max:
                max = a*b

    print(max)


if __name__ == '__main__':
    main()
