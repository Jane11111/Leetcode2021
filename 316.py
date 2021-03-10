# -*- coding: utf-8 -*-
# @Time    : 2021-03-09 14:01
# @Author  : zxl
# @FileName: 316.py


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s


        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c]+=1







