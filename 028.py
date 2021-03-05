# -*- coding: utf-8 -*-
# @Time    : 2021-03-02 11:53
# @Author  : zxl
# @FileName: 028.py

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        l = len(needle)
        res = -1
        for i in range(len(haystack)):
            if haystack[i:i+l] == needle:
                res = i
                break
        return res

obj = Solution()
haystack = "hello"
needle = "ll"
res = obj.strStr(haystack,needle)
print(res)

