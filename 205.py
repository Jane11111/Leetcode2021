# -*- coding: utf-8 -*-
# @Time    : 2021-06-18 13:19
# @Author  : zxl
# @FileName: 205.py



class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s)!=len(t) :
            return False

        s_dic = {}
        t_dic = {}
        for i in range(len(s)):
            if s[i] not in s_dic and t[i] not in t_dic:
                s_dic[s[i]] = t[i]
                t_dic[t[i]] = s[i]
            elif s[i] not in s_dic or t[i] not in t_dic:
                return False
            else:
                if s_dic[s[i]] != t[i]:
                    return False
        return True
