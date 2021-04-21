# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 22:54
# @Author  : zxl
# @FileName: 187.py


class Solution:
    def findRepeatedDnaSequences(self, s: str) :

        dic = {}

        for i in range(len(s)-9):
            tmp = s[i:i+10]
            if tmp  not in dic:
                dic[tmp] = 1
            else:
                dic[tmp]+=1
        lst = []
        for k in dic:
            if dic[k]>1:
                lst.append(k)
        return lst