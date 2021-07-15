# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 10:59
# @Author  : zxl
# @FileName: 032_6.py


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        arr = [-1 for i in range(len(s))]

        st = []

        for i in range(len(s)):

            if s[i] == '(':
                st.append(i)
            else:
                if len(st):
                    idx = st.pop()
                    arr[idx] = i

        ans = 0

        i = 0
        while i<len(s):

            if arr[i] == -1:
                i+=1
            else:
                j = arr[i]+1
                while j<len(s) and arr[j]!=-1:
                    j = arr[j]+1
                ans = max(ans,j-i)
                i = j
        return ans



