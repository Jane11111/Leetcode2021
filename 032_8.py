# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 11:35
# @Author  : zxl
# @FileName: 032_8.py


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        left_count = 0
        right_count = 0

        ans = 0

        for c in s:
            if c == '(':
                left_count+=1
            else:
                right_count+=1

            if left_count == right_count :
                ans = max(ans,left_count*2)
            if right_count >left_count:
                left_count = 0
                right_count = 0
        left_count = 0
        right_count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == '(':
                left_count +=1
            else:
                right_count+=1
            if left_count == right_count:
                ans = max(ans,left_count*2)
            if left_count>right_count:
                left_count = 0
                right_count = 0
        return ans


