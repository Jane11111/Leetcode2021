# -*- coding: utf-8 -*-
# @Time    : 2021-03-08 17:08
# @Author  : zxl
# @FileName: Offer016.py

import sys
sys.setrecursionlimit(1000000)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n==0:
            return 1
        if n== 1 :
            return x
        if x == 0:
            return 0

        if n < 0:
            n = -n
            x = 1/x

        m1 = self.myPow(x,int(n/2))
        m2 = self.myPow(x,int(n%2))

        return m1*m2*m1

x = 2
n = 10
obj = Solution()
res =obj.myPow(x,n)
print(res)
