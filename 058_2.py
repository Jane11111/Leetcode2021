# -*- coding: utf-8 -*-
# @Time    : 2021-07-14 15:04
# @Author  : zxl
# @FileName: 058_2.py


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        ans = 0
        i = len(s)-1
        while i>=0 and s[i] == ' ':
            i-=1
        while i>=0 and s[i]!=' ':
            i-=1
            ans+=1
        return ans

