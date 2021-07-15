# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 11:20
# @Author  : zxl
# @FileName: 032_7.py



class Solution:
    def longestValidParentheses(self, s: str) -> int:


        arr = [0 for i in range(len(s))]

        left_count = 0
        for i in range(len(s)):
            if s[i] == '(':
                left_count+=1
            else:
                if left_count == 0:
                    arr[i] = -1
                else:
                    left_count-=1
        right_count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ')':
                right_count+=1
            else:
                if right_count==0:
                    arr[i] = -1
                else:
                    right_count-=1

        ans = 0
        count = 0
        for i in range(len(s)):
            if arr[i] == -1:
                count = 0
            else:
                count+=1
            ans = max(ans,count)
        return ans


