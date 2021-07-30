# -*- coding: utf-8 -*-
# @Time    : 2021-07-11 18:41
# @Author  : zxl
# @FileName: 028_4.py

class Solution:


    def createTable(self,needle):

        n = len(needle)
        arr = [0 for i in range(n)]

        for i in range(1,len(needle)):
            j = arr[i-1]
            while j>0 and needle[j]!=needle[i]:
                j = arr[j-1]

            if needle[j] == needle[i]:
                arr[i] = j+1
        return arr


    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) == 0:
            return 0

        arr = self.createTable(needle)
        j = 0
        i = 0

        while i<len(haystack):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            else:
                if j == 0:
                    i+=1
                else:
                    j = arr[j-1]
            if j == len(needle):
                return i-len(needle)
        return -1

obj = Solution()
haystack = "hello"
needle = "ll"
ans = obj.strStr(haystack,needle)
print(ans)

