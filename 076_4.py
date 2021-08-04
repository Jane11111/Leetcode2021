# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 19:26
# @Author  : zxl
# @FileName: 076_4.py


class Solution:
    def minWindow(self, s: str, t: str) -> str:


        tdic = {}
        sdic = {}

        tcount= 0
        for c in t:
            if c not in tdic:
                tdic[c] = 0
            tdic[c]+=1
            if tdic[c] == 1:
                tcount+=1

        p = 0
        i = 0
        ccount=0
        ans = ''
        while i<len(s):

            c = s[i]
            if c not in sdic:
                sdic[c] = 0
            sdic[c]+=1
            if c in tdic and sdic[c] == tdic[c]:
                ccount +=1
            while ccount == tcount:
                if len(s[p:i+1]) < len(ans) or ans == '':
                    ans = s[p:i+1]
                sdic[s[p]]-=1
                if s[p] in tdic and sdic[s[p]] <tdic[s[p]]:
                    ccount -= 1
                p+=1

            i+=1
        return ans
