# -*- coding: utf-8 -*-
# @Time    : 2021-07-19 11:22
# @Author  : zxl
# @FileName: 435_3.py



class Solution:
    def eraseOverlapIntervals(self, intervals ) -> int:

        intervals.sort()

        i = 0

        last_end = float('-inf')
        count = 0

        for s,e in intervals:

            if s<last_end:
                count+=1
                last_end = min(last_end,e)
            else:
                last_end = e
        return count



