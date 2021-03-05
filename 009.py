# -*- coding: utf-8 -*-
# @Time    : 2021-03-02 10:03
# @Author  : zxl
# @FileName: 009.py

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        res = True

        i = 0
        j = len(s) - 1

        while i <= len(s) - 1 and j >= 0 and i<j:
            if s[i] != s[j]:
                res = False
            i+=1
            j-=1
        return res



obj = Solution()
x = -101
res = obj.isPalindrome(x)
print(res)
