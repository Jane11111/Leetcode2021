# -*- coding: utf-8 -*-
# @Time    : 2021-05-24 14:24
# @Author  : zxl
# @FileName: 032_4.py



class Solution:
    def longestValidParentheses(self, s: str) -> int:

        ans = 0
        left = 0
        right = 0
        for c in s:
            if c == '(':
                left+=1
            else:
                right+=1
            if left == right:
                ans = max(2*left,ans)
            elif left<right:
                left = 0
                right = 0
        left = 0
        right = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == '(':
                left+=1
            else:
                right+=1
            if left == right:
                ans = max(ans,2*left)
            elif left>right:
                left = 0
                right = 0
        return ans

