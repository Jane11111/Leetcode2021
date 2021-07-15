# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 09:25
# @Author  : zxl
# @FileName: 029_3.py




class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        pos = True

        if dividend < 0 and divisor < 0:
            pos = True
            dividend = abs(dividend)
            divisor = abs(divisor)
        elif dividend < 0:
            pos = False
            dividend = abs(dividend)
        elif divisor < 0:
            pos = False
            divisor = abs(divisor)


        base  = divisor
        v = 1

        ans = 0

        while dividend>=divisor:

            if dividend>=base:
                dividend-=base
                ans+=v
                base+=base
                v+=v
            else:
                base = divisor
                v = 1
        if not pos:
            ans=-ans
        if ans< - 2**31:
            ans  = -2**31
        if ans> 2**31-1:
            ans = 2**31-1
        return ans







