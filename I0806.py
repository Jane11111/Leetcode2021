# -*- coding: utf-8 -*-
# @Time    : 2021-03-08 14:09
# @Author  : zxl
# @FileName: I0806.py


class Solution(object):
    def hanota(self, A, B, C):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :rtype: None Do not return anything, modify C in-place instead.
        """
        if len(A) == 0:
            return

        n = A.pop(0)
        self.hanota(A,[],B)
        C.append(n)
        self.hanota(B,A,C)


A = [4,2,1,0]

B = []
C = []

obj = Solution()
obj.hanota(A,B,C)
print(A)
print(B)
print(C)