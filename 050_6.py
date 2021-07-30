# -*- coding: utf-8 -*-
# @Time    : 2021-07-30 13:17
# @Author  : zxl
# @FileName: 050_6.py



class Solution:
    def myPow(self, x: float, n: int) -> float:


        if x == 0:
            return 0

        if n<0:
            x = 1/x
            n = -n

        base = x

        val = 1

        while n:

            if n%2:
                val*=base
            base*=base
            n//=2
        return val







