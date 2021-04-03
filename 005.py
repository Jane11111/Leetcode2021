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

        m = len(s)
        dp = []
        for i in range(m):
            dp.append([False for j in range(m)])
            dp[i][i] = True
        ans = s[0]
        max_len = 1
        for l in range(2,m+1,1):
            for i in range(m):
                j = i+l-1
                if j>= m:
                    break
                if s[i]==s[j] :
                    if i+1 >= j-1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if j-i+1 > max_len:
                            max_len = j-i+1
                            ans = s[i:j+1]

        return ans



obj = Solution()
s = "ac"
res = obj.longestPalindrome(s)
print(res)
