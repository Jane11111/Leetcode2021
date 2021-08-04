# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 10:54
# @Author  : zxl
# @FileName: 056_4.py

class Solution:
    def merge(self, intervals ) :


        intervals.sort()


        lst = []
        i = 0
        while i<len(intervals):

            min_val = intervals[i][0]
            max_val = intervals[i][1]

            i+=1
            while i<len(intervals) and intervals[i][0]<=max_val:
                max_val = max(max_val,intervals[i][1])
                i+=1
            lst.append([min_val,max_val])
        return lst




