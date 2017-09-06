# -*- coding: utf-8 -*-

# Tip 29 Using property instead of get and set

class Register(object):
    def __init__(self, name, age):
        self._name = name
        self.age = age
        self.logo = self._name + "," + str(self.age)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        """You can do something more than just setting property in this method"""
        self._name = name  # Do not use self.name = name, it will raise max recursive exception
        self.logo = self._name + "," + str(self.age)


if __name__ == '__main__':
    r = Register('Niko', 18)
    r.name = 'Belic'
    print r.logo
