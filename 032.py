# -*- coding: utf-8 -*-
# @Time    : 2021-04-28 20:32
# @Author  : zxl
# @FileName: 032.py

class Solution:
    def longestValidParentheses(self, s: str) -> int:

        char_stack = []
        idx_stack = []
        arr = [-1 for i in range(len(s))]
        i = 0
        while i<len(s):

            if s[i] == '(':
                char_stack.append(s[i])
                idx_stack.append(i)
            else:
                if len(char_stack)>0 and char_stack[-1] == '(':
                    char_stack.pop()
                    arr[idx_stack.pop()] = i
                # else:
                #     char_stack.append(')')
            i +=1
        max_val = 0
        i = 0
        while i<len(s):
            if arr[i] !=-1:
                j = arr[i]+1
                while j<len(s) and arr[j]!=-1:
                    j = arr[j]+1
                max_val = max(max_val,j-i)
                i = j
            else:
                i+=1
        return max_val

obj = Solution()
s = "(()"
ans = obj.longestValidParentheses(s)
print(ans)



