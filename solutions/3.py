#!/usr/bin/env python

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


def gcd(a, b):
    """Recursive implementation of Euler's GCD algorithm"""

    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def factorize(num):
    """Using the Pollard-Rho algorithm"""

    # https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
