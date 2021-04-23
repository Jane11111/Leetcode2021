# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 22:16
# @Author  : zxl
# @FileName: Offer003.py


class Solution:
    def findRepeatNumber(self, nums )  :
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] =True
            else:
                return n