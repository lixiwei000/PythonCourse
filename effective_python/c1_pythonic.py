#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tip1: Check Your Python Version Before Starting Work
from flask import json


def py_version():
    import sys
    print sys.version


# Tip2: Following PEP8 Coding Stype
def pep8_style():
    pass


# Tip3: Knowing Bytes、Str、Unicode
def str_and_unicode():
    """
    In Python3: Str.encode() -> Bytes, Bytes.decode() -> Str
    In Python2: Unicode.encode() -> Str, Str.decode() -> Unicode
    """
    my_unicode = u'你好'
    my_str = my_unicode.encode('utf-8')
    print my_str


# Tip7: Using List Generator Instead Of Map & Filter
def list_generator():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sqr_list_gen = [x ** 2 for x in a]
    sqr_lambda = map(lambda x: x ** 2, a)
    sqr_list_gen_with_condition = [x ** 2 for x in a if x % 2 == 0]
    sqr_map_filter = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, a))
    print sqr_list_gen
    print sqr_lambda
    print sqr_list_gen_with_condition
    print sqr_map_filter
    print "============== Pretty Split Line =============="
    chile_ranks = {'tom': 1, 'helen': 2, 'harry_porter': 3}
    rank_dict = {rank: name for name, rank in chile_ranks.items()}  # Dict Generator
    print rank_dict
    print "============== Pretty Split Line =============="
    chile_len_set = {len(name) for name in rank_dict.values()}
    print chile_len_set


# Tip8: Don't Using List Generator More Than Twice With One Time
def more_list_generator():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # flat = [e for row in matrix for e in row]
    flat = [[x for x in row] for row in matrix]
    print flat
    sqr = [[e ** 2 for e in row] for row in matrix]
    print sqr

    my_lists = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ]
    # Write Multiple Lines While Using Multiple List Generators
    flat = [x for s1 in my_lists
            for s2 in s1
            for x in s2]
    print flat

    # Multiple Conditions While Creating List
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = [x for x in a if x > 4 if x % 2 == 0]
    print b

    # Find The Elements Whose RowSum >= 10 And Element % 3 == 0
    filtered = [[x for x in row if x % 3 == 0] for row in matrix if sum(row) >= 10]
    # filtered = [e for row in matrix if sum(row) >= 10 for e in row if e % 3 == 0]
    print filtered


# Tip9: Generator Expression
def generator_expression():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l_it = (x for x in l)
    sqr_it = ((x, x ** 2) for x in l_it)
    for x in sqr_it:
        print x


# Tip10: Enumerate
def enum_instead_of_range():
    from random import randint
    # Range Is Useful while Handle Integers
    random_bits = 0
    for i in range(64):
        if randint(0, 1):
            random_bits |= 1 << i
    print "============== Pretty Split Line =============="

    flavor_list = ['coco', 'coke', 'KungPaoKiTen', 'Banana']
    for flavor_index in range(len(flavor_list)):
        print '%d : %s is delicious' % (flavor_index + 1, flavor_list[flavor_index])

    print "============== Pretty Split Line =============="

    for i, flavor in enumerate(flavor_list, 1):
        print '%d : %s is delicious' % (i, flavor)


# Tip11: Zip
def iterator_multiple_collections_by_zip():
    names = ['Niko', 'Tom', 'Helen']
    ages = [21, 15, 25]
    sizes = {'A': 35, 'B': 60, 'C': 22}
    for name, age, size, in zip(names, ages, sizes):
        print name, age, size


# Tip12: For Else
def for_else():
    num_list = [x for x in range(100)]
    for n in num_list:
        print n
        if n == 20:
            break
    else:
        print 'for never break.'

# Tip13: Try Except Else Finally
def try_excep_else_finally():
    f = open('/Users/lixiwei-mac/Documents/IdeaProjects/PythonStudy/effective_python/test.txt', 'r')
    try:
        data = f.read()
        if len(data) < 100:
            raise Exception("Shit ! This fucking file is too short")
    except Exception as e:
        raise ValueError(e)
    else:
        print 'There is no exception happend.'
        print data
        return data
    finally:
        print 'closing file handle'
        f.close()


if __name__ == "__main__":
    try_excep_else_finally()
