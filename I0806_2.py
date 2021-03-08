# -*- coding: utf-8 -*-
# @Time    : 2021-03-08 15:51
# @Author  : zxl
# @FileName: I0806_2.py


class Solution(object):


    def move(self,n,A,B,C):
        if n == 0:
            return

        num = A[-n]
        self.move(n-1,A,C,B)
        C.append(num)
        A.pop(-1)
        self.move(n-1,B,A,C) # 移动的只是借用B的那么n-1个，即使B中原来有圆盘，也没有关系

    def hanota(self, A, B, C):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :rtype: None Do not return anything, modify C in-place instead.
        """

        self.move(len(A),A,B,C)

A = [4,3,2,1,0]

B = []
C = []

obj = Solution()
obj.hanota(A,B,C)
print(A)
print(B)
print(C)