# -*- coding: utf-8 -*-
# @Time    : 2021-04-14 16:33
# @Author  : zxl
# @FileName: 622.py

class MyCircularQueue:

    def __init__(self, k: int):

        self.k = k
        self.cq = [0 for i in range(k)]
        self. head = 0
        self.tail = k-1
        self.size = 0


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.tail = (self.tail+1)%self.k
        # print(self.tail)
        self.cq[self.tail] = value
        self.size+=1

        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head+1)%self.k
        self.size-=1
        return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.cq[self.head]


    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.cq[self.tail]


    def isEmpty(self) -> bool:
        return self.size == 0


    def isFull(self) -> bool:
        return self.size==self.k