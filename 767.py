# -*- coding: utf-8 -*-
# @Time    : 2021-03-11 20:57
# @Author  : zxl
# @FileName: 767.py


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """

        if len(S) <= 1:
            return S

        m = (len(S)+1)//2
        dic = {}
        for s in S:
            if s not in dic:
                dic[s] = 0
            dic[s]+=1
            if dic[s]>m:
                return ""




