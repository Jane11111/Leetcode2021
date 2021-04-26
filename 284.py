# -*- coding: utf-8 -*-
# @Time    : 2021-04-26 22:41
# @Author  : zxl
# @FileName: 284.py


#
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
        self.lst = []

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if len(self.lst)==0:
            self.lst.append(self.iter.next())
        return self.lst[0]


    def next(self):
        """
        :rtype: int
        """
        if len(self.lst)>0:
            return self.lst.pop(0)
        else:
            return self.iter.next()



    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.lst)>0 or self.iter.hasNext()
