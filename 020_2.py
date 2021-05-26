# -*- coding: utf-8 -*-
# @Time    : 2021-05-16 21:46
# @Author  : zxl
# @FileName: 020_2.py


class Solution:
    def isValid(self, s: str) -> bool:


        st = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                st.append(c)
            else:
                if len(st) == 0:
                    return False
                last = st.pop()
                if (c==')' and last == '(') or (c==']' and last == '[') or (c=='}' and last == '{') :
                    continue
                else:
                    return False
        return len(st) == 0
