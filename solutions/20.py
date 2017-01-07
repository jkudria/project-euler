#!/usr/bin/env python

# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!


def factorial(n):
    """Recursive factorial implementation"""

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    """Main entry point"""

    print(sum([int(x) for x in str(factorial(100))]))

if __name__ == '__main__':
    main()
