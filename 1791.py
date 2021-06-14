# -*- coding: utf-8 -*-
# @Time    : 2021-06-09 10:07
# @Author  : zxl
# @FileName: 1791.py



class Solution:
    def findCenter(self, edges ) -> int:


        dic = {}
        for x,y in edges[:2]:
            if x not in dic:
                dic[x] = 0
            if y not in dic:
                dic[y] = 0
            dic[x]+=1
            dic[y]+=1
        for k in dic:
            if dic[k] == 2:
                return k