# -*- coding: utf-8 -*-
# @Time    : 2021-06-14 14:48
# @Author  : zxl
# @FileName: Offer041.py



class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []

    def findPos(self,lst,num):

        if len(lst)== 0:
            return 0

        l = 0
        r = len(lst)-1
        stop = False
        while l<= r and not stop:
            m = (l+r)//2
            if l == r:
                stop = True
            if lst[m]<=num:
                l = m+1
            else:
                r = m

        return l


    def addNum(self, num: int) -> None:

        i = self.findPos(self.lst,num)
        self.lst.insert(i,num)



    def findMedian(self) -> float:

        n = len(self.lst)
        if n%2 == 1:
            m = int(n/2)
            return self.lst[m]
        else:
            m1 = int(n/2)
            m2 = m1-1
            return (self.lst[m1]+self.lst[m2])/2
