# -*- coding: utf-8 -*-
# @Time    : 2021-06-14 11:11
# @Author  : zxl
# @FileName: 028_3.py



class Solution:

    def getTmpTable(self,needle):

        dp = [0 for i in range(len(needle))]

        for i in range(1,len(needle)):
            j= dp[i-1]
            while j>0 and needle[i]!= needle[j]:
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

        j = 0 # 指向needle中下一个匹配的点
        for i in range(len(haystack)):

            while j>0 and haystack[i]!= needle[j]:
                j = dp[j-1]
            if haystack[i] == needle[j]:
                j+=1
            if j == len(needle):
                return i-len(needle)+1
        return -1

obj = Solution()
haystack = "hello"

needle = "ll"
ans = obj.strStr(haystack,needle)
print(ans)