# -*- coding: utf-8 -*-
# @Time    : 2021-05-19 11:04
# @Author  : zxl
# @FileName: 050.py


class Solution:
    def myPow(self, x: float, n: int) -> float:

        ans = 1
        neg = False
        if n <0:
            neg = True
            n = -n

        while n>0:
            if n%2 == 1:
                ans*=x
            n//=2
            x*=x
        if neg:
            ans = 1/ans
        return ans
