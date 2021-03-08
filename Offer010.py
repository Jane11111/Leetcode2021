# -*- coding: utf-8 -*-
# @Time    : 2021-03-08 14:01
# @Author  : zxl
# @FileName: Offer010.py


class Solution(object):

    def recursiveCal(self,n,dic):
        if n==0:
            return 1
        if n < 0:
            return 0

        if n in dic:
            return dic[n]
        if n-1 in dic:
            l = dic[n-1]
        else:
            l = self.recursiveCal(n-1,dic)
            dic[n-1] = l

        if n-2 in dic:
            r = dic[n-2]
        else:
            r = self.recursiveCal(n-2,dic)
            dic[n-2] = r
        return l+r

    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.recursiveCal(n,{})%1000000007
