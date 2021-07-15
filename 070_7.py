# -*- coding: utf-8 -*-
# @Time    : 2021-07-14 16:54
# @Author  : zxl
# @FileName: 070_7.py


class Solution:
    def climbStairs(self, n: int) -> int:


        if n == 1:
            return 1
        if n == 2:
            return 2

        a = 1
        b = 2
        for i in range(3,n+1):
            c = a+b
            a = b
            b = c
        return b