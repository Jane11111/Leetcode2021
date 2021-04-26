# -*- coding: utf-8 -*-
# @Time    : 2021-04-25 21:45
# @Author  : zxl
# @FileName: 260.py

class Solution:
    def singleNumber(self, nums )  :

        x = 0
        for num in nums:
            x^=num

        n = 1
        while not x%2 ==1:
            x//=2
            n*=2

        a = 0
        b = 0
        for num in nums:
            if num&n == 0:
                a^=num
            else:
                b^=num
        return [a,b]
