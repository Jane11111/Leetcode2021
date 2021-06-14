# -*- coding: utf-8 -*-
# @Time    : 2021-06-13 16:05
# @Author  : zxl
# @FileName: 231.py



class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        num = 1
        while num<=n:
            if num == n:
                return True
            num *= 2
        return False