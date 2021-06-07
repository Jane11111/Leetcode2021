# -*- coding: utf-8 -*-
# @Time    : 2021-06-04 16:18
# @Author  : zxl
# @FileName: 020_3.py



class Solution:
    def isValid(self, s: str) -> bool:

        st = []
        for c in s:
            if c == '(' or c == '[' or c=='{':
                st.append(c)
            else:
                if len(st)==0:
                    return False
                if c == ')':
                    if st[-1]=='(':
                        st.pop()
                    else:
                        return False
                if c == ']':
                    if st[-1]=='[':
                        st.pop()
                    else:
                        return False
                if c == '}':
                    if st[-1] == '{':
                        st.pop()
                    else:
                        return False
        return len(st)==0






