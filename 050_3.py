# -*- coding: utf-8 -*-
# @Time    : 2021-07-13 22:55
# @Author  : zxl
# @FileName: 050_3.py




class Solution:


    def recurSolve(self,x,n):
        if abs(n) == 1:
            if n<0:
                return 1/x
            return x

        ans = self.recurSolve(x,(abs(n)//2)*(-1 if n<0 else 1)) ** 2

        if n%2:
            if n<0:
                ans *= (1/x)
            else:
                ans*=x
        return ans




    def myPow(self, x: float, n: int) -> float:

        if x == 0:
            return 0
        if n == 0:
            return 1
        # if n<0:
        #     return 1/self.recurSolve(x,-n)
        return self.recurSolve(x,n)

