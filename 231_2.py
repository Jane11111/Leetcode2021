# -*- coding: utf-8 -*-
# @Time    : 2021-06-13 16:07
# @Author  : zxl
# @FileName: 231_2.py


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n<=0:
            return False

        return n&(n-1)==0
