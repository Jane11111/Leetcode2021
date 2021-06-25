# -*- coding: utf-8 -*-
# @Time    : 2021-06-24 21:43
# @Author  : zxl
# @FileName: 409.py



class Solution:
    def longestPalindrome(self, s: str) -> int:


        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c]+=1
        ans = 0
        largest_num = 0
        for c in dic:
            ans += (dic[c]//2)*2

        if ans <len(s):
            ans += 1
        return ans


