# -*- coding: utf-8 -*-
# @Time    : 2021-03-06 23:25
# @Author  : zxl
# @FileName: 1137_2.py


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

        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)


obj = Solution()
n = 25
print(obj.tribonacci(n))