# -*- coding: utf-8 -*-
# @Time    : 2021-03-15 10:53
# @Author  : zxl
# @FileName: 392_2.py


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)

        i = 0
        j = 0
        while i<m and j<n:
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                j+=1
        return i==m


obj = Solution()
s = "axe"
t = "abcde"
ans = obj.isSubsequence(s,t)
print(ans)