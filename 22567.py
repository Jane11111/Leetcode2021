# -*- coding: utf-8 -*-
# @Time    : 2021-06-13 15:22
# @Author  : zxl
# @FileName: 22567.py

class MyQueue:

    def __init__(self):
        self.lst = []


    def push(self,x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop(0)
    def top(self):
        return self.lst[0]

    def empty(self):
        return len(self.lst)==0

    def size(self):
        return len(self.lst)


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = MyQueue()
        self.q2 = MyQueue()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """

        if self.q2.empty():
            self.q2.push(x)
            while not self.q1.empty():
                self.q2.push(self.q1.pop())
        else:
            self.q1.push(x)
            while not self.q2.empty():
                self.q1.push(self.q2.pop())




    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.q1.empty():
            return self.q1.pop()
        else:
            return self.q2.pop()



    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.q1.empty():
            return self.q1.top()
        else:
            return self.q2.top()




    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q1.empty() and self.q2.empty()