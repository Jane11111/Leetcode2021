# -*- coding: utf-8 -*-
# @Time    : 2021-04-28 20:47
# @Author  : zxl
# @FileName: 032_2.py


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        arr = [0 for i in range(len(s))]

        my_stack = []
        for i in range(len(s)):
            if s[i] == '(':
                my_stack.append(i)
            else :
                if len(my_stack) == 0:
                    arr[i] = 1
                else:
                    my_stack.pop()
        while len(my_stack)>0:
            arr[my_stack.pop()] = 1

        max_val = 0
        i = 0
        while i<len(arr):
            if arr[i] == 1:
                i+=1
            else:
                j = i+1
                while j<len(arr) and arr[j] == 0:
                    j+=1
                max_val = max(max_val,j-i)
                i = j
        return max_val
