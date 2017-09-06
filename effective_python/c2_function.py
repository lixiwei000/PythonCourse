#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tip15: Closure
from itertools import islice


def sort_priority(values, group):
    def helper(x):
        if x in group:
            return 0, x
        return 1, x

    values.sort(key=helper)


def sort_priority_v2(values, group):
    found = [False]  # 位于此作用于的列表、元组、字典可以被内部函数搜索并修改

    def helper(x):
        # python3中可以使用nonlocal来在此处声明found，以表示查找并修改外层作用域的found
        if x in group:
            found[0] = True
        if found:
            return 0, x
        return 1, x

    values.sort(key=helper)
    return found


def do_sort_proority():
    nums = [2, 5, 6, 5, 4, 7, 45, 54, 8]
    group = {2, 4, 45, 8}
    found = sort_priority_v2(nums, group)
    print nums
    print found


# Tip16: Generator
def get_first_letter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


def do_get_first_letter():
    # for index in get_first_letter('Niko Belic Is A Good Boy'):
    #     print index

    # print list(get_first_letter('Niko Belic Is A Good Boy'))

    index_iterator = get_first_letter('Niko Belic Is A Good Boy')
    print list(islice(index_iterator, 0, 3))


# Tip17: Iter
def normalize(numbers):
    total = sum(numbers)  # return a new iterator
    result = []

    for value in numbers:  # return a new iterator
        percent = 100 * value / total
        result.append(percent)
    return result


class ReadVisits:
    def __init__(self, numbers):
        self.numbers = numbers

    def __iter__(self):
        for value in self.numbers:
            yield value


def do_nomalize():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    visits = ReadVisits(numbers)
    print normalize(numbers)
    print iter(visits) is iter(visits)


# Tip19: Params
def flow_rate(weight_diff, time_diff, period=1, units_per_kg=1):
    return ((weight_diff * units_per_kg) / time_diff) * period

def test(a,b):
    return 1

def do_calc_flow_rate():
    print flow_rate(10, 5)
    print flow_rate(10, 5)


if __name__ == '__main__':
    do_nomalize()
