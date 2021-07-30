# -*- coding: utf-8 -*-
# @Time    : 2021-07-19 11:44
# @Author  : zxl
# @FileName: 1288_2.py



class Solution:
    def removeCoveredIntervals(self, intervals ) -> int:


        for i in range(len(intervals)):
            intervals[i][1] = - intervals[i][1]

        intervals.sort()
        for i in range(len(intervals)):
            intervals[i][1] = -intervals[i][1]



        i = 0
        max_val = float('-inf')
        count = 0

        while i<len(intervals):

            if intervals[i][1]<=max_val:

                count+=1
            # else:
            max_val = max(max_val,intervals[i][1])

            i+=1
        return len(intervals)-count


