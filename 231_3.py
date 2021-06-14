# -*- coding: utf-8 -*-
# @Time    : 2021-06-13 16:17
# @Author  : zxl
# @FileName: 231_3.py


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n<=0:
            return False

        return (2**30)%n == 0
