#!/usr/bin/env python

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


def seive(n):
    """
    Generates all primes up to n, based on
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Overview
    """

    primes = list(range(2, n))
    index = 0  # will start out to represent the value of 2

    while index < len(primes):
        value = primes[index]  # this is the value we seive
        print(value)

        # technically this can all be done with a list comp but I couldn't figure one out

        # index + 1 avoids the value itself and the list before that doesn't
        # need to be checked
        for prime in primes[index + 1:]:
            if prime % value == 0:
                print("  {prime}".format(prime=prime))
                primes.remove(prime)  # will raise ValueError. Might need to deal

        index += 1  # this will take the next element in the list which is a prime

    return primes


def main():
    print(sum(seive(2000000)))


if __name__ == '__main__':
    main()
