# -*- coding: utf-8 -*-
# @Time    : 2021-07-14 09:02
# @Author  : zxl
# @FileName: SHIEN02.py


class Solution:
    def strStr(self , haystack , needle ):

        if needle == '':
            return 0

        n = len(needle)
        count = 0
        for i in range(len(haystack)):
            if haystack[i:i+n] == needle:
                return i
        return -1



obj = Solution()
haystack = 'shein'
needle = 'in'
ans = obj.strStr(haystack,needle)
print(ans)