# -*- coding: utf-8 -*-
# @Time    : 2021-07-02 16:49
# @Author  : zxl
# @FileName: 380.py

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

        if val not in self.dict or self.dict[val]<0:
            if val not in self.dict or self.dict[val] == -1: # 已经pop出去了
                self.lst.append(val)
            self.dict[val] = 1
            return True
        return False


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dict or self.dict[val] <0:
            return False

        self.dict[val] = -2 # 延迟pop
        return True




    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """

        p = random.randrange(0,len(self.lst))
        while not self.dict[self.lst[p]]>0:
            v = self.lst[p]

            self.lst[p] = self.lst[-1]
            self.dict[v] = -1 # 已经pop出去了
            self.lst.pop()
            p = random.randrange(0, len(self.lst))
        return self.lst[p]




