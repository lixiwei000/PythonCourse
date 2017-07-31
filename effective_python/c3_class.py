#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from collections import defaultdict
# Tip23: simple api should accept functions but not instance
from threading import Thread

from flask import json


def simple_api():
    added_count = [0]

    def missing():
        added_count[0] += 1  # In Python3 ,We Can Use "nonlocal added_count to use outer fields."
        return 0

    current = {'a': 1, 'b': 2, 'c': 3}
    # current = defaultdict(lambda: 0, current) # Way One.
    # current = defaultdict(missing, current) # Way Two.
    missing_counter = MissingCounter()
    current = defaultdict(missing_counter, current)  # Way Three.

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


# Tip24: classmethod

# Traditional: if we need another type of data source,we have to rewrite generate_inputs & create_workers & mapreduce
class InputData(object):
    def __init__(self):
        pass

    def read(self):
        raise NotImplementedError


# class PathInputData(InputData):
#     def __init__(self, path):
#         self.path = path
#
#     def read(self):
#         return open(self.path).read()



class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


# class SpaceCounterWork(Worker):
#     def map(self):
#         data = self.input_data.read()
#         self.result = data.count(' ')
#         print data, self.result
#
#     def reduce(self, other):
#         self.result += other.result


def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(SpaceCounterWork(input_data))

    return workers


def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result


# def map_reduce(data_dir):
#     inputs = generate_inputs(data_dir)
#     workers = create_workers(inputs)
#     return execute(workers)
#
# def do_map_reduce():
#     data_dir = "data"
#     result = map_reduce(data_dir)
#     print result


# Generic Version

class GenericInputData():
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(GenericInputData):
    def __init__(self, path):
        self.path = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker():
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class SpaceCounterWork(GenericWorker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count(' ')
        print data, self.result

    def reduce(self, other):
        self.result += other.result


def map_reduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)


def do_map_reduce():
    data_dir = "data"
    config = {'data_dir': data_dir}
    result = map_reduce(SpaceCounterWork, PathInputData, config)
    print result


# Tip25: Init super class


class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class TimesFiveCorrect(MyBaseClass):
    def __init__(self, value):
        super(TimesFiveCorrect, self).__init__(value)
        self.value *= 5


class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super(PlusTwoCorrect, self).__init__(value)
        self.value += 2


class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        super(GoodWay, self).__init__(value)


def test_super():
    gw = GoodWay(2)
    from pprint import pprint
    # MRO: Method Resolution Order
    '''
    [<class '__main__.GoodWay'>,
     <class '__main__.TimesFiveCorrect'>,
     <class '__main__.PlusTwoCorrect'>,
     <class '__main__.MyBaseClass'>,
     <type 'object'>]
     构造器调用关系如上，上层调用下层，因此下层类的构造器是最先初始化的
    '''
    pprint(GoodWay.mro())

    print 'It should be (2 * 5) + 2 = 12,but actually is ', gw.value


# Tip26: Using mix in components while using multiple extends
class ToDictMixin(object):
    def to_dict(self):
        return self._tranverse_dict(self.__dict__)

    def _tranverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._tranverse(key, value)
        return output

    def _tranverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._tranverse_dict(value)
        elif isinstance(value, list):
            return [self._tranverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._tranverse_dict(value.__dict__)
        else:
            return value


class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTreeWithParent(BinaryTree):
    def __init__(self, value, left=None, right=None, parent=None):
        super(BinaryTreeWithParent, self).__init__(value, left=left, right=right)
        self.parent = parent

    def _tranverse(self, key, value):
        if isinstance(value, BinaryTree) and key == 'parent':
            return value.value
        else:
            return super(BinaryTreeWithParent, self)._tranverse(key, value)


def do_trans():
    root = BinaryTreeWithParent(0)
    root.left = BinaryTreeWithParent(1, parent=root)
    root.left.right = BinaryTreeWithParent(2, parent=root)
    print json.dumps(root.to_dict())


class JsonMixin(object):
    @classmethod
    def from_json(cls, data):
        kwargs = json.loads(data)
        return cls(**kwargs)

    def to_json(self):
        return json.dumps(self.to_dict())


class DatacenterRack(ToDictMixin, JsonMixin):
    def __init__(self,name,age):
        self.name = name
        self.age = age



def do_serialize():
    serialized_data = '''
    {
      "name":"李熙伟",
      "age":20
    }
    '''
    deserialized_data = DatacenterRack.from_json(serialized_data)
    print type(deserialized_data)
    print deserialized_data.to_json()

# Tips28: Using collection.abc while extending collections

if __name__ == '__main__':
    do_serialize()
