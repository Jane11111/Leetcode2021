# -*- coding: utf-8 -*-
# @Time    : 2021-02-14 16:36
# @Author  : zxl
# @FileName: 005.py


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 0
        res = ''
        for i in range(len(s)):
            l = i
            r = i
            while l>=0 and r <= len(s)-1 :

                if s[l] != s[r]:
                    break
                l -= 1
                r += 1

            if l-r+1 > max_len:
                res = s[l:r+1]
                max_len = l-r+1

            l = i
            r = i+1
            while l >= 0 and r <= len(s) - 1 :

                if s[l] != s[r]:
                    break
                l -= 1
                r += 1

            if l-r+1 > max_len:
                res = s[l:r+1]
                max_len = l-r+1
        return res

obj = Solution()
s = 'babad'
res = obj.longestPalindrome(s)
print(res)
