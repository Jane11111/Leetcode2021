# -*- coding: utf-8 -*-
# @Time    : 2021-05-26 15:37
# @Author  : zxl
# @FileName: Offer010-1.py


class Solution:
    def fib(self, n: int) -> int:


        if n<2:
            return n

        n1 = 0
        n2 = 1

        for i in range(2,n+1):
            tmp = n2
            n2 = (n1+n2)%1000000007
            n1 = tmp
        return n2