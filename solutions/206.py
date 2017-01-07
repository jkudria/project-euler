#!/usr/bin/env python

"""
Problem:
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""
import math



def main():
    # Brutefore solution - we check all numbers that fit the pattern

    done = False

    # ewwwwww
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            for g in range(10):
                                for h in range(10):
                                    for i in range(10):
                                        string = f'1{a}2{b}3{c}4{d}5{e}6{f}7{g}8{h}9{i}0'
                                        square = int(string)
                                        print(string)

                                        z += 1

                                        sqrt = math.sqrt(square)
                                        if (square % 1) == 0.0:
                                            break

    print(sqrt)


if __name__ == '__main__':
    main()
