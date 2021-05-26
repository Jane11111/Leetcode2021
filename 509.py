# -*- coding: utf-8 -*-
# @Time    : 2021-05-16 15:58
# @Author  : zxl
# @FileName: 509.py



class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1
        n1 = 0
        n2 = 1
        for i in range(2,n+1):
            tmp = n1+n2
            n1 = n2
            n2 = tmp
        return n2