# -*- coding: utf-8 -*-
# @Time    : 2021-03-06 23:19
# @Author  : zxl
# @FileName: 1137.py

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        res = 0
        l1 = 0
        l2 = 1
        l3 = 1
        for i in range(3,n+1,1):
            res = l1 + l2 + l3
            l1 = l2
            l2 = l3
            l3 = res
        return res

obj = Solution()
n = 25
print(obj.tribonacci(n))