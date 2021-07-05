# -*- coding: utf-8 -*-
# @Time    : 2021-07-04 15:31
# @Author  : zxl
# @FileName: 003_3.py


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        ans = 0
        l = 0
        dic = {}
        for i in range(len(s)):
            c = s[i]
            if c not in dic:
                dic[c] = 0
            dic[c] += 1
            while dic[c]>1:

                dic[s[l]]-=1
                l += 1
            ans = max(ans,i-l+1)
        return ans

