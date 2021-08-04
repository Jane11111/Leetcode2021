# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 16:11
# @Author  : zxl
# @FileName: 069_9.py


class Solution:
    def mySqrt(self, x: int) -> int:

        l = 0
        h = x

        while l<h:
            m = (l+h+1)//2

            if m*m>x:
                h = m-1
            else:
                l = m
        return l

