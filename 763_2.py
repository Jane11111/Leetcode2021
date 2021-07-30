# -*- coding: utf-8 -*-
# @Time    : 2021-07-19 11:37
# @Author  : zxl
# @FileName: 763_2.py


class Solution:
    def partitionLabels(self, s: str) :

        dic = {}

        for i in range(len(s)):
            dic[s[i]] = i

        ans = []
        i = 0
        while i<len(s):

            max_len = dic[s[i]]

            j = i+1
            while j<len(s) and j<=max_len:
                max_len=max(max_len,dic[s[j]])
                j+=1
            ans.append(j-i)

            i=j
        return ans


