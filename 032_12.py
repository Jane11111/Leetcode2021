# -*- coding: utf-8 -*-
# @Time    : 2021-07-26 16:24
# @Author  : zxl
# @FileName: 032_12.py


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        left = 0
        right = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                left+=1
            elif s[i] == ')':
                right+=1

            if left == right:
                ans = max(ans,2*left)
            if right>left:
                left = 0
                right = 0
        left = 0
        right = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == '(':
                left+=1
            elif s[i] == ')':
                right+=1

            if left == right:
                ans = max(ans,2*left)
            if left>right:
                left  = 0
                right = 0
        return ans

