# -*- coding: utf-8 -*-
# @Time    : 2021-06-13 15:47
# @Author  : zxl
# @FileName: 232_2.py


class MyStack():

    def __init__(self):
        self.lst = []

    def push(self,x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def peek(self):
        return self.lst[-1]

    def empty(self):
        return len(self.lst)==0

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st1 = MyStack()
        self.st2 = MyStack()



    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.st1.push(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.st2.empty():
            return self.st2.pop()
        else:
            while not self.st1.empty():
                self.st2.push(self.st1.pop())
            return self.st2.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.st2.empty():
            return self.st2.peek()
        else:
            while not self.st1.empty():
                self.st2.push(self.st1.pop())
            return self.st2.peek()


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """

        return self.st1.empty() and self.st2.empty()
