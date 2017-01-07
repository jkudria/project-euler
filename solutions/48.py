#!/usr/bin/env python

print(sum(x**x for x in range(1, 1001)) % 10_000_000_000)
