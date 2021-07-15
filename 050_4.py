# -*- coding: utf-8 -*-
# @Time    : 2021-07-13 22:56
# @Author  : zxl
# @FileName: 050_4.py

class Solution:

    def myPow(self, x: float, n: int) -> float:

        if x == 0:
            return 0
        if n == 0:
            return 1

        if n<0:
            x = 1/x
        n = abs(n)

        ans = 1
        val = x
        while n:
            if n%2:
                ans*=val
            val*=val
            n//=2
        return ans
