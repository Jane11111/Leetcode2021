# -*- coding: utf-8 -*-
# @Time    : 2021-06-18 15:56
# @Author  : zxl
# @FileName: 367.py

class Solution:
    def isPerfectSquare(self, num: int) -> bool:


        for i in range(num+1):
            if i*i == num:
                return True
            if i*i > num:
                return False


