# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 17:31
# @Author  : zxl
# @FileName: 044_3.py



class Solution:


    def memoRecur(self,s,p,dic):
        if p in dic and s in dic[p]:
            return dic[p][s]

        if p not in dic:
            dic[p] = {}

        if s == '' and p == '':
            return True
        if p == '':
            return False
        if s == '':
            for i in range(len(p)):
                if p[i]!='*':
                    dic[p][s] = False
                    return False
            dic[p][s] = True
            return True
        if p[0] == '?':
            f = self.memoRecur(s[1:],p[1:],dic)

        elif p[0] == '*':
            f1 = self.memoRecur(s,p[1:],dic)
            f2 = self.memoRecur(s[1:],p[1:],dic)
            f3 = self.memoRecur(s[1:],p,dic)
            f = f1 or f2 or f3
        else:
            f = (p[0] == s[0]) and self.memoRecur(s[1:],p[1:],dic)
        dic[p][s] = f
        return f



    def isMatch(self, s: str, p: str) -> bool:

        dic = {}
        ans = self.memoRecur(s,p,dic)
        return ans


