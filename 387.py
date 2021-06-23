# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 22:04
# @Author  : zxl
# @FileName: 387.py


class Solution:
    def firstUniqChar(self, s: str) -> int:

        dic = {}
        for c in s:
            if c not in dic:
                dic[c]=1
            else:
                dic[c]+=1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1


