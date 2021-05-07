# -*- coding: utf-8 -*-
# @Time    : 2021-05-07 11:52
# @Author  : zxl
# @FileName: Offer066.py


class Solution:
    def constructArr(self, a )  :

        lst = [1 for i in range(len(a))]

        x = 1
        for i in range(len(a)):
            lst[i] = x
            x*=a[i]

        y = 1
        for i in range(len(a)-1,-1,-1):
            lst[i] *=y
            y*=a[i]
        return lst


