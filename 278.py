# -*- coding: utf-8 -*-
# @Time    : 2021-04-25 22:08
# @Author  : zxl
# @FileName: 278.py


def isBadVersion(version):
    return True


class Solution:

    def biSearch(self,i,j):
        if i>j:
            return -1
        if i==j:
            if isBadVersion(i):
                return i
            else:
                return -1

        m = (i+j)//2
        if isBadVersion(m):
            num = self.biSearch(i,m-1)
            if num==-1:
                return m
            else:
                return num
        else:
            num = self.biSearch(m+1,j)
            return num




    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        return self.biSearch(1,n)

