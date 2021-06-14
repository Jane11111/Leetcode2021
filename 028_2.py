# -*- coding: utf-8 -*-
# @Time    : 2021-06-13 17:04
# @Author  : zxl
# @FileName: 028_2.py


class Solution:

    def getTmpTable(self,needle):
        dp = [0 for i in range(len(needle))]

        j = 0
        for i in range(1,len(needle)):
            while j>0 and needle[i]!=needle[j]:
                j = dp[j-1]
            if needle[i] == needle[j]:
                j+=1
            dp[i] = j


        return dp


    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) == 0:
            return 0

        if len(haystack) == 0:
            return -1

        dp = self.getTmpTable(needle)

        j = 0
        for i in range(len(haystack)):
            while j>0 and haystack[i]!=needle[j]:
                j = dp[j-1]
            if haystack[i] == needle[j]:# 下一次j从哪里开始
                j+=1
            if j == len(needle):
                return i-len(needle)+1
        return -1

obj = Solution()
haystack = "mississippi"

needle = "issip"
ans = obj.strStr(haystack,needle)
print(ans)



