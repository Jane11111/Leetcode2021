# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 09:23
# @Author  : zxl
# @FileName: 029_2.py

# TODO 超时

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        pos = True

        if dividend <0 and divisor<0:
            pos = True
            dividend = abs(dividend)
            divisor = abs(divisor)
        elif dividend<0:
            pos = False
            dividend = abs(dividend)
        elif divisor<0:
            pos = False
            divisor = abs(divisor)


        count = 0

        while dividend>=divisor:
            dividend-=divisor
            count+=1
        if not pos:
            count = -count
        return count

