# -*- coding: utf-8 -*-
# @Time    : 2021-08-02 11:28
# @Author  : zxl
# @FileName: 1754_2.py




class Solution:

    def largestMerge(self, word1: str, word2: str) -> str:

        i = 0
        j = 0
        s = ''

        while i<len(word1) or j <len(word2):
            if i>=len(word1):
                s+=word2[j:]
                j = len(word2)
            elif j>=len(word2):
                s+=word1[i:]
                i = len(word1)

            elif word1[i]>word2[j]:
                s+=word1[i]
                i+=1
            elif word2[j]>word1[i]:
                s+=word2[j]
                j+=1
            else:
                if word1[i:]>=word2[j:]:
                    s+=word1[i]
                    i+=1
                else:
                    s+=word2[j]
                    j+=1
        return s





