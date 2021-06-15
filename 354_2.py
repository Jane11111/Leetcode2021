# -*- coding: utf-8 -*-
# @Time    : 2021-06-15 21:29
# @Author  : zxl
# @FileName: 354_2.py




class Solution:

    def biSearch(self,lst,target):
        if len(lst) == 0 or target>lst[-1]:
            return len(lst)
        l = 0
        r = len(lst)-1
        while l<r:
            m = (l+r)//2
            if target == lst[m]:
                return m
            if target<lst[m]:
                r = m
            else:
                l = m+1
        return l

    def maxEnvelopes(self, envelopes ) -> int:


        for i in range(len(envelopes)):
           envelopes[i][1] = -envelopes[i][1]


        envelopes.sort()

        for i in range(len(envelopes)):
            envelopes[i][1] = -envelopes[i][1]



        lst = [envelopes[0][1]]

        for i in range(1,len(envelopes)):

            pos = self.biSearch(lst,envelopes[i][1])
            if pos == len(lst):
                lst.append(envelopes[i][1])
            else:
                lst[pos] = envelopes[i][1]



        return len(lst)


