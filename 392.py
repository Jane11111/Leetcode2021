# -*- coding: utf-8 -*-
# @Time    : 2021-03-15 09:24
# @Author  : zxl
# @FileName: 392.py


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)

        r = []
        for i in range(m+1):
            r.append([False for j in range(n+1)])
        for i in range(n+1):
            r[0][i] = True
        for i in range(1,m+1):
            r[i][0] = False

        for i in range(m):
            for j in range(n):

                if s[i] == t[j]:
                    r[i+1][j+1] = r[i][j]

                else:
                    r[i+1][j+1] = r[i+1][j]
        return r[m][n]

obj = Solution()
s = "ace"
t = "abcde"
ans = obj.isSubsequence(s,t)
print(ans)

