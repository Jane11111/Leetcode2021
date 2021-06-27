# -*- coding: utf-8 -*-
# @Time    : 2021-06-25 13:50
# @Author  : zxl
# @FileName: 424.py



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        dic = {chr(ord('A')+i):0 for i in range(26)}

        historyMax = 0

        for r in range(len(s)):

            dic[s[r]] += 1
            historyMax = max(historyMax,dic[s[r]])

            if historyMax+k < r-l+1:
                l+=1
                dic[s[l-1]] -=1
        return len(s)-l

