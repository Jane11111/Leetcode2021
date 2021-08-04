# -*- coding: utf-8 -*-
# @Time    : 2021-08-02 10:57
# @Author  : zxl
# @FileName: 1754.py


class Solution:

    def recSolve(self,word1,word2,   dic):

        if word1 in dic and word2 in dic[word1]:
            return dic[word1][word2]

        if len(word1)>len(word2):
            return self.recSolve(word2,word1,dic)

        if word1 not in dic:
            dic[word1] = {}


        if len(word1) == 0 and len(word2) == 0:
            return ''
        if len(word1) == 0:
            s = word2
        elif len(word2)== 0:
            s = word1
        else:
            if word1[0]>word2[0]:
                s = word1[0]+self.recSolve(word1[1:],word2,dic)
            elif word1[0]<word2[0]:
                s = word2[0]+self.recSolve(word1,word2[1:],dic)
            else:
                s1 = word1[0]+self.recSolve(word1[1:],word2,dic)
                s2 = word2[0]+self.recSolve(word1,word2[1:],dic)
                s = max(s1,s2)
        dic[word1][word2] = s
        return dic[word1][word2]



    def largestMerge(self, word1: str, word2: str) -> str:


        ans = self.recSolve(word1,word2, {})
        return ans



