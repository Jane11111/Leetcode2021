# -*- coding: utf-8 -*-
# @Time    : 2021-04-26 22:50
# @Author  : zxl
# @FileName: 284_2.py


class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.peek_num = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if  self.peek_num:
            return self.peek_num
        self.peek_num = self.iter.next()
        return self.peek_num


    def next(self):
        """
        :rtype: int
        """
        if self.peek_num:
            num = self.peek_num
            self.peek_num=None
            return num
        else:
            return self.iter.next()



    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peek_num!=None or self.iter.hasNext()
