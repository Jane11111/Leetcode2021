# -*- coding: utf-8 -*-
# @Time    : 2021-04-18 12:32
# @Author  : zxl
# @FileName: 066.py


class Solution:
    def plusOne(self, digits )  :

        base = 1
        i = len(digits)-1
        while i>=0 and base!=0:
            v = digits[i]+base
            digits[i] = v%10
            base = v//10
            i-=1
        if base!=0:
            digits.insert(0,base)
        return digits

obj = Solution()
digits = [9,9,9]
ans = obj.plusOne(digits)
print(ans)