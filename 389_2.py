# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 22:09
# @Author  : zxl
# @FileName: 389_2.py



class Solution:
    def findTheDifference(self, s: str, t: str) -> str:


        n1 = 0
        n2 = 0
        for c in s:
            n1+=ord(c)
        for c in t:
            n2 += ord(c)

        diff = n2-n1
        c = chr(diff)
        return c

obj = Solution()
s = 'abcd'
t = 'abcde'
ans = obj.findTheDifference(s,t)
print(ans)
