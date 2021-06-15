# -*- coding: utf-8 -*-
# @Time    : 2021-06-15 21:24
# @Author  : zxl
# @FileName: 354.py


class Solution:
    def maxEnvelopes(self, envelopes ) -> int:


        envelopes.sort()
        dp = [1 for i in range(len(envelopes))]

        for i in range(len(envelopes)):
            for j in range(i ):
                if envelopes[i][0]>envelopes[j][0] and envelopes[i][1]>envelopes[j][1]:
                    dp[i] = max(dp[i],dp[j]+1)


        return max(dp)
