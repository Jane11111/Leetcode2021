# -*- coding: utf-8 -*-
# @Time    : 2021-05-23 16:21
# @Author  : zxl
# @FileName: 032_3.py


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        st = []
        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
            else:
                if len(st)>0 and s[st[-1]] == '(':
                    st.pop()
                else:
                    st.append(i)
        arr = [0 for i in range(len(s))]
        for idx in st:
            arr[idx] = 1

        ans = 0
        i = 0
        while i<len(s):
            if arr[i] == 1:
                i+=1
            else:
                j = i+1
                while j<len(s) and arr[j]==0:
                    j+=1
                ans = max(ans,j-i)

                i = j
        return ans