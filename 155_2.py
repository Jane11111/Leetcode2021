# -*- coding: utf-8 -*-
# @Time    : 2021-04-02 21:12
# @Author  : zxl
# @FileName: 155_2.py


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []

    def push(self, val: int) -> None:
        if len(self.lst) == 0:
            self.lst.append(val)
            self.lst.append(val)
        else:
            self.lst.append(min(val,self.lst[-2]))
            self.lst.append(val)


    def pop(self) -> None:
        self.lst = self.lst[:-2]

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return self.lst[-2]
