# -*- coding: utf-8 -*-
# @Time    : 2021-07-26 22:11
# @Author  : zxl
# @FileName: 300_7.py





class Solution:

    def insert(self,lst,val):
        if len(lst)==0 or val>lst[-1]:
            lst.append(val)
            return

        l = 0
        h = len(lst)-1

        while l<h:
            m = (l+h)//2
            if lst[m]<val:
                l = m+1
            else:
                h = m
        lst[l] = val
        return


    def lengthOfLIS(self, nums ) -> int:

        lst = []

        for num in nums:
            self.insert(lst,num)

        return len(lst)

