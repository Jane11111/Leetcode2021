# -*- coding: utf-8 -*-
# @Time    : 2021-08-04 10:19
# @Author  : zxl
# @FileName: 087_3.py

class Solution:


    def recJudge(self,s1,s2,dic):

        if s1 in dic and s2 in dic[s1]:
            return dic[s1][s2]
        if s1 not in dic:
            dic[s1] = {}

        if len(s1) == 1:
            dic[s1][s2] = s1== s2
            return dic[s1][s2]

        for i in range(len(s1)-1):

            f1 = self.recJudge(s1[:i+1],s2[:i+1],dic)
            f2 = self.recJudge(s1[i+1:],s2[i+1:],dic)

            if f1 and f2:
                dic[s1][s2] = True
                return True

            f3 = self.recJudge(s1[:i+1],s2[-(i+1):],dic)
            f4 = self.recJudge(s1[i+1:],s2[:-(i+1)],dic)

            if f3 and f4:
                dic[s1][s2] = True
                return True
        dic[s1][s2] = False
        return False


    def isScramble(self, s1: str, s2: str) -> bool:

        dic = {}
        ans = self.recJudge(s1,s2,dic)
        return ans





