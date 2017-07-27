#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict


# Tip23: simple api should accept functions but not instance
def simple_api():
    added_count = [0]

    def missing():
        added_count[0] += 1  # In Python3 ,We Can Use "nonlocal added_count to use outer fields."
        return 0

    current = {'a': 1, 'b': 2, 'c': 3}
    # current = defaultdict(lambda: 0, current) # Way One.
    # current = defaultdict(missing, current) # Way Two.
    missing_counter = MissingCounter()
    current = defaultdict(missing_counter, current) # Way Three.

    increment = [('d', 4), ('e', 5), ('f', 6)]
    print 'Before Increment', current
    for desc, num in increment:
        current[desc] += num
    print 'After Increment', current
    # print 'Total Missing Key Count', added_count[0]
    print 'Total Missing Key Count', missing_counter.missing_count


class MissingCounter:
    def __init__(self):
        self.missing_count = 0

    def __call__(self, *args, **kwargs):
        self.missing_count += 1
        return 0


if __name__ == '__main__':
    simple_api()
