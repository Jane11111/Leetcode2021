# -*- coding: utf-8 -*-
# @Time    : 2021-03-09 09:33
# @Author  : zxl
# @FileName: 155.py
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self. lst = []


    def push(self, val: int) -> None:

        self.lst.append(val)




    def pop(self) -> None:
        self.lst = self.lst[:-1]


    def top(self) -> int:
        return self.lst[-1]


    def getMin(self) -> int:

        i = 0
        val = self.lst[0]
        while i<len(self.lst):
            val = min(val,self.lst[i])
            i+=1
        return val


