#!/usr/bin/env python

# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
# 20 letters. The use of "and" when writing out numbers is in compliance with
# British usage.


def parse_two_digit(i, letter_counts):
    """Parses a two digit number and counts the letters used to write it out"""

    return_count = 0
    if i in letter_counts:
        return_count = letter_counts[i]
    else:
        tens, ones = tuple([int(char) for char in str(i)])
        # after the tuple 72 would be 7, 2. We need to turn the tens, 7,
        # into 70
        tens *= 10

        return_count += letter_counts[tens]
        return_count += letter_counts[ones]

    return return_count


def main():
    """Main entry point"""

    # I could use some setattr magic, but I don't really like doing that. I'll
    # hard code it for now

    letter_counts = {
        # 0 because when parsing three digits I don't want the trailing zeros
        # to cause any problems
        0: 0,
        1: len('one'),
        2: len('two'),
        3: len('three'),
        4: len('four'),
        5: len('five'),
        6: len('six'),
        7: len('seven'),
        8: len('eight'),
        9: len('nine'),
        10: len('ten'),

        # the teens can theoretically be composed of 'teen' and
        # something else, but in practice, it's less of a hassle
        # to just manually hardcode each one - too many
        # non-trivial ones (e.g. eleven, twelve, thirteen, etc.)
        11: len('eleven'),
        12: len('twelve'),
        13: len('thirteen'),
        14: len('fourteen'),
        15: len('fifteen'),
        16: len('sixteen'),
        17: len('seventeen'),
        18: len('eighteen'),
        19: len('nineteen'),

        # tens
        20: len('twenty'),
        30: len('thirty'),
        40: len('forty'),
        50: len('fifty'),
        60: len('sixty'),
        70: len('seventy'),
        80: len('eighty'),
        90: len('ninety'),
    }

    letter_count = 0
    # two digits
    for i in range(1, 100):
        letter_count += parse_two_digit(i, letter_counts)

    for i in range(100, 1000):
        # all will have this:
        letter_count += len('hundred')

        hundreds = int(str(i)[0])
        two_digit_part = int(str(i)[1:])

        if two_digit_part != 0:
            letter_count += len('and')

        letter_count += letter_counts[hundreds]
        letter_count += parse_two_digit(two_digit_part, letter_counts)

    letter_count += len('onethousand')

    print(letter_count)


if __name__ == '__main__':
    main()
