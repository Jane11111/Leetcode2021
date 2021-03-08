# -*- coding: utf-8 -*-
# @Time    : 2021-03-08 17:03
# @Author  : zxl
# @FileName: I0805.py


class Solution(object):



    def multiply(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: int
        """
        if A > B:
            tmp = A
            A = B
            B = tmp
        if A == 0:
            return A
        if A == 1:
            return B
        return B + self.multiply(A-1,B)

A = 4
B = 3
obj = Solution()
res = obj.multiply(A,B)
print(res)