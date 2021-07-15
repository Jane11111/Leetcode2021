# -*- coding: utf-8 -*-
# @Time    : 2021-07-13 22:24
# @Author  : zxl
# @FileName: 050_2.py


class Solution:
    def myPow(self, x: float, n: int) -> float:


        if n == 0:
            return 1
        if x == 0:
            return 0

        pos = True
        if n<0:
            pos = False
            n = abs(n)

        base = 1
        val = x
        ans = 1

        while n:
            if base>n:
                base = 1
                val = x
            ans*=val
            n-=base
            base*=2
            val*=val
        if not pos:
            ans = 1/ans
        return ans
