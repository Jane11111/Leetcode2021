# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 22:55
# @Author  : zxl
# @FileName: Offer009.py


class mystack():
    def __init__(self):
        self.lst = []
    def insert(self,x):
        self.lst.append(x)
    def pop(self):
        return self.lst.pop()
    def is_empty(self):
        return len(self.lst) == 0

class CQueue:

    def __init__(self):

        self.lst1 = mystack()
        self.lst2 = mystack()


    def appendTail(self, value: int) -> None:
        self.lst1.insert(value)


    def deleteHead(self) -> int:

        if self.lst1.is_empty() and self.lst2.is_empty():
            return -1
        if not self.lst2.is_empty():
            return self.lst2.pop()
        while not self.lst1.is_empty():
            self.lst2.insert(self.lst1.pop())
        return self.lst2.pop()

