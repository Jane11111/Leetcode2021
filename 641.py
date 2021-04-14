# -*- coding: utf-8 -*-
# @Time    : 2021-04-14 16:50
# @Author  : zxl
# @FileName: 641.py


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.cdq = [0 for i in range(k)]
        self.head = 1
        self.tail = -1
        self.size = 0
        self.k = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.head = (self.head+self.k-1)%self.k
        self.cdq[self.head] = value
        self.size+=1
        if self.size == 1:
            self.tail = self.head
        return True




    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.tail = (self.tail+1)%self.k
        self.cdq[self.tail] = value
        self.size+=1
        if self.size == 1:
            self.head = self.tail
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.head = (self.head +1)%self.k

        self.size-=1
        return True



    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.tail = (self.tail + self.k-1)%self.k
        self.size-=1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.cdq[self.head]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.cdq[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0


    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.k