# -*- coding: utf-8 -*-
# @Time    : 2021-06-03 22:02
# @Author  : zxl
# @FileName: 125.py




class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s)-1

        while i<j:
            if not s[i].isalpha() and not s[i].isnumeric():
                i+=1
            elif not s[j].isalpha() and not s[j].isnumeric():
                j-=1
            else:
                c1 = s[i]
                c2 = s[j]
                if c1.isalpha():
                    c1 = c1.lower()
                if c2.isalpha():
                    c2 = c2.lower()
                if c1!=c2:
                    return False
                i+=1
                j-=1
        return True