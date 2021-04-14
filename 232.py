# -*- coding: utf-8 -*-
# @Time    : 2021-04-13 22:08
# @Author  : zxl
# @FileName: 232.py

class myStack():

    def __init__(self):
        self.lst = []

    def push(self,v):
        self.lst.append(v)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)

    def empty(self):
        return len(self.lst) == 0

    def peek(self):
        return self.lst[-1]

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst1 = myStack()
        self.lst2 = myStack()


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """

        self.lst1.push(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """

        if self.lst2.size()>0:
            return self.lst2.pop()
        else:
            while self.lst1.size()>0:
                self.lst2.push(self.lst1.pop())
            return self.lst2.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.lst2.size()>0:
            return self.lst2.peek()
        else:
            while self.lst1.size()>0:
                self.lst2.push(self.lst1.pop())
            return self.lst2.peek()


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.lst1.empty() and self.lst2.empty()
