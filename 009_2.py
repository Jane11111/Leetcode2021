# -*- coding: utf-8 -*-
# @Time    : 2021-07-05 11:15
# @Author  : zxl
# @FileName: 009_2.py

class Solution:
    def isPalindrome(self, x: int) -> bool:


        if x<0:
            return False

        s = str(x)
        i = 0
        j = len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True




