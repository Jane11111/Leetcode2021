# -*- coding: utf-8 -*-
# @Time    : 2021-07-14 13:50
# @Author  : zxl
# @FileName: 056_2.py


class Solution:
    def merge(self, intervals ) :


        intervals.sort()

        ans = []

        i = 0
        while i<len(intervals):
            min_val = intervals[i][0]
            max_val = intervals[i][1]

            i+=1
            while i<len(intervals) and intervals[i][0]<=max_val:
                max_val = max(max_val,intervals[i][1])
                i+=1
            ans.append([min_val,max_val])
        return ans