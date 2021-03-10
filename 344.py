# -*- coding: utf-8 -*-
# @Time    : 2021-03-10 14:00
# @Author  : zxl
# @FileName: 344.py


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while i<j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i+=1
            j-=1