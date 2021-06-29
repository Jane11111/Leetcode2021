# -*- coding: utf-8 -*-
# @Time    : 2021-06-29 16:08
# @Author  : zxl
# @FileName: 214_2.py


class Solution:
    def shortestPalindrome(self, s: str) -> str:

        base = 131
        mod = 1000000007

        h1 = 0
        h2 = 0
        mul = 1
        l = 0

        for i in range(len(s)):

            n = ord(s[i])

            h1 = h1*base+n
            h2 = h2+n*(mul)
            h1 %= mod
            h2 %= mod

            if h1 == h2:
                l = i+1
            mul*=base


        new_s = s
        for i in range(l,len(s)):
            new_s = s[i]+new_s
        return new_s
obj = Solution()
s = "aacecaaa"
ans = obj.shortestPalindrome(s)
print(ans)