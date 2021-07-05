# -*- coding: utf-8 -*-
# @Time    : 2021-07-02 17:52
# @Author  : zxl
# @FileName: 381.py

import random

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.lst = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        f = False
        self.lst.append(val)
        if val not in self.dict or len(self.dict[val]['lst']) == 0:
            f = True
            if val not in self.dict:
                self.dict[val ]  = {'lst':[],'lst_idx':{}}

        self.dict[val]['lst'].append(len(self.lst)-1)
        self.dict[val]['lst_idx'][len(self.lst)-1] = len(self.dict[val]['lst'])-1


        return f




    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.dict or len(self.dict[val]['lst']) == 0:
            return False

        idx = self.dict[val]['lst'][-1] # O(1) 找到某个index 把这个idx的val删除掉
        new_val = self.lst[-1]  # 新的value
        self.lst[idx] = new_val

        # 先把new_val 的index 改变了，

        new_val_removed_idx_in_dict = self.dict[new_val]['lst_idx'][len(self.lst)-1] # 新的value删除掉的idx 在dict中的位置


        self.dict[new_val]['lst'][new_val_removed_idx_in_dict] = idx
        self.dict[new_val]['lst_idx'][idx] = new_val_removed_idx_in_dict

        # 再把最后一个val pop出去，并且更新val对应的dict中的index

        self.lst.pop()
        idx_in_dict = self.dict[val]['lst_idx'][idx]
        new_idx = self.dict[val]['lst'][-1]
        self.dict[val]['lst'][idx_in_dict] = new_idx
        self.dict[val]['lst'].pop()
        self.dict[val]['lst_idx'][new_idx] = idx_in_dict



        return True


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """

        p = random.randrange(0,len(self.lst))
        return self.lst[p]