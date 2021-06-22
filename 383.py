# -*- coding: utf-8 -*-
# @Time    : 2021-06-21 17:34
# @Author  : zxl
# @FileName: 383.py



class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:



        dic = {}
        for c in magazine:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c]+=1
        for c  in ransomNote:
            if c not in dic or dic[c]<=0:
                return False
            dic[c]-=1
        return True