# -*- coding: utf-8 -*-
# @Time    : 2021-06-17 22:26
# @Author  : zxl
# @FileName: 202.py

class Solution:
    def isHappy(self, n: int) -> bool:

        dic = {n: True}

        while n != 1:
            # print(n)
            v = 0
            while n:
                v += (n % 10) ** 2
                n //= 10
            if v in dic:
                return False
            dic[v] = True
            n = v

        return True