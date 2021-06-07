# -*- coding: utf-8 -*-
# @Time    : 2021-06-02 14:25
# @Author  : zxl
# @FileName: 633.py


import numpy as np
class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        m = int(np.sqrt(c))+1
        i = 0
        j = m
        while i<=j:
            num = i**2+j**2

            if num==c:
                return True
            elif num<c:
                i+=1
            else:
                j-=1
        return False


