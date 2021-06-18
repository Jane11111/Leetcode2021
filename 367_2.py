# -*- coding: utf-8 -*-
# @Time    : 2021-06-18 15:58
# @Author  : zxl
# @FileName: 367_2.py


class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        l = 0
        r = num
        while l < r:
            m = (l + r) // 2
            # if m*m == num:
            #     return True
            if m * m < num:
                l = m + 1
            else:
                r = m
        return l ** 2 == num

