# -*- coding: utf-8 -*-
# @Time    : 2021-07-02 17:16
# @Author  : zxl
# @FileName: 380_2.py


import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.lst = []



    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dict or self.dict[val] == -1:
            self.lst.append(val)
            self.dict[val] = len(self.lst)-1
            return True
        return False


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

        if val not in self.dict or self.dict[val] == -1:
            return False
        idx = self.dict[val]
        self.lst[idx] = self.lst[-1]



        self.dict[self.lst[idx]] = idx # 更新这个item的idx
        self.dict[val] = -1
        self.lst.pop()

        return True




    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """

        idx = random.randrange(0,len(self.lst))
        return self.lst[idx]

