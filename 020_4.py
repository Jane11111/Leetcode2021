# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 17:04
# @Author  : zxl
# @FileName: 020_4.py



class Solution:
    def isValid(self, s: str) -> bool:

        st = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                st.append(c)
            else:
                if c == ')':
                    if len(st)>0 and st[-1] == '(':
                        st.pop()
                    else:
                        return False
                elif c == ']':
                    if len(st)>0 and st[-1] == '[':
                        st.pop()
                    else:
                        return False
                elif c == '}':
                    if len(st)>0 and st[-1] == '{':
                        st.pop()
                    else:
                        return False
        return len(st)==0