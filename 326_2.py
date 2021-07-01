# -*- coding: utf-8 -*-
# @Time    : 2021-07-01 09:51
# @Author  : zxl
# @FileName: 326_2.py



import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        max_num = 3**(int(math.log(n,3))+1)
        return n>0 and max_num%n == 0


