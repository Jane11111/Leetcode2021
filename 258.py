# -*- coding: utf-8 -*-
# @Time    : 2021-04-25 21:42
# @Author  : zxl
# @FileName: 258.py


class Solution:
    def addDigits(self, num: int) -> int:

        n = 0

        while num>=10:

            while num:
                n+=num%10
                num//=10
            num = n
            n = 0
        return num