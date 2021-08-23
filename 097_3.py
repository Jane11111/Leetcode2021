# -*- coding: utf-8 -*-
# @Time    : 2021-08-04 16:01
# @Author  : zxl
# @FileName: 097_3.py


class Solution:
    def recFind(self,s1,s2,s3,dic):
        if s1 in dic and s2 in dic[s1]:
            return dic[s1][s2]

        if len(s1) == 0 and len(s2) == 0:
            return True

        if s1 not in dic:
            dic[s1] = {}


        if len(s1) and s1[0] == s3[0]:
            f = self.recFind(s1[1:],s2,s3[1:],dic)
            if f:
                dic[s1][s2] = True
                return f
        if len(s2) and s2[0] == s3[0]:
            f = self.recFind(s1,s2[1:],s3[1:],dic)
            if f:
                dic[s1][s2] = True
                return f
        dic[s1][s2] = False
        return False



    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:


        if len(s1)+len(s2) != len(s3):
            return False

        ans = self.recFind(s1,s2,s3,{})
        return ans


