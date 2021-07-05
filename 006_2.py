# -*- coding: utf-8 -*-
# @Time    : 2021-07-05 10:26
# @Author  : zxl
# @FileName: 006_2.py

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        lst = ['' for i in range(numRows)]

        r = 0
        op = 1
        for i in range(len(s)):
            lst[r]+=s[i]
            if r == numRows-1:
                op = -1
            elif r == 0:
                op = 1
            r+=op
        new_s = ''.join(lst)
        return new_s


