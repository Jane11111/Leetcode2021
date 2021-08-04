# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 16:14
# @Author  : zxl
# @FileName: 069_10.py


class Solution:
    def mySqrt(self, n: int) -> int:

        xk = n

        while xk**2 -n > 1e-4:
            xk = xk - (xk**2-n)/(2*xk)
        return int(xk)





