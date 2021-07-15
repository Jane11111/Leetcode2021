# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 09:34
# @Author  : zxl
# @FileName: 030_2.py


class Solution:

    def check(self,s,idx,words):

        dic = {word:0 for word in words}
        for word in words:
            dic[word] += 1

        n = len(words)
        k = len(words[0])

        for i in range(idx,idx+n*k,k):
            if s[i:i+k] not in dic or dic[s[i:i+k]] <=0:
                return False
            dic[s[i:i+k]] -=1
        return True



    def findSubstring(self, s: str, words ) :



        ans = []

        for i in range(len(s)):
            if self.check(s,i,words):
                ans.append(i)
        return ans




