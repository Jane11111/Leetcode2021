# -*- coding: utf-8 -*-
# @Time    : 2021-07-30 13:14
# @Author  : zxl
# @FileName: 050_5.py



class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1
        if x == 0:
            return 0


        if n<0:
            x = 1/x
            n = -n
        if n == 1:
            return x

        if n%2 == 0:
            return self.myPow(x,n//2)**2

        return x*self.myPow(x,n//2)**2

