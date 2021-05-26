# -*- coding: utf-8 -*-
# @Time    : 2021-05-15 12:08
# @Author  : zxl
# @FileName: 069_6.py




class Solution:

    def mySqrt(self, x: int) -> int:




        xk = x

        while abs(xk**2-x)>1e-3:
            xk = xk-((xk**2-x)/(2*xk))
        return int(xk)