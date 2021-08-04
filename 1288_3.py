# -*- coding: utf-8 -*-
# @Time    : 2021-07-30 22:53
# @Author  : zxl
# @FileName: 1288_3.py



class Solution:
    def removeCoveredIntervals(self, intervals ) -> int:

        for i in range(len(intervals)):
            intervals[i][1] = -intervals[i][1]

        intervals.sort()

        for i in range(len(intervals)):
            intervals[i][1] = -intervals[i][1]

        max_val = float('-inf')
        count = 0

        for s,e in intervals:
            if e<= max_val:
                count+=1
            max_val = max(max_val,e)
        return len(intervals)-count



