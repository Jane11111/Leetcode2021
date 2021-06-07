# -*- coding: utf-8 -*-
# @Time    : 2021-06-07 10:41
# @Author  : zxl
# @FileName: 171.py




class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        if len(columnTitle) == 0:
            return 0


        base = len(columnTitle)

        ans = 0

        for i in range(len(columnTitle)):

            num = ord(columnTitle[i])-ord('A')+1

            ans += num*(26**(base-i-1))
        return ans

