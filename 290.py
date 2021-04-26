# -*- coding: utf-8 -*-
# @Time    : 2021-04-25 22:26
# @Author  : zxl
# @FileName: 290.py




class Solution:

    def judge(self,dic,lst):
        if len(set(lst)) != len(dic):
            return False

        for k in dic:
            v = lst[dic[k][0]]
            for idx in dic[k]:
                if lst[idx] != v:
                    return False
        return True



    def wordPattern(self, pattern: str, s: str) -> bool:

        n1 = len(pattern)
        lst = s.split(' ')
        n2 = len(lst)
        if n2<n1 or n2%n1!=0:
            return False
        dic = {}
        for i in range(n1):
            if pattern[i] not in dic:
                dic[pattern[i]] = []
            dic[pattern[i] ].append(i)

        for i in range(0,n2,n1):
            f = self.judge(dic,lst[i:i+n1])
            if not f:
                return f
        return True
