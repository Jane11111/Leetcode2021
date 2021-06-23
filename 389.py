# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 22:07
# @Author  : zxl
# @FileName: 389.py


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:


        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c]+=1

        for c in t:
            if c not in dic or dic[c] == 0:
                return c
            dic[c]-=1



