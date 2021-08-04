# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 11:00
# @Author  : zxl
# @FileName: 057_3.py




class Solution:
    def insert(self, intervals , newInterval )  :


        intervals.sort()

        # if newInterval[0]>intervals[-1][1]:
        #     intervals.append(newInterval)
        #     return intervals


        lst = []
        i = 0
        inserted = False
        while i<len(intervals):

            if inserted:
                lst.append(intervals[i])
                i+=1
                continue
            if newInterval[1]<intervals[i][0]:
                lst.append(newInterval)
                lst.append(intervals[i])
                inserted = True
                i+=1
            elif newInterval[0]>intervals[i][1]:
                lst.append(intervals[i])
                i+=1
            else:
                min_val = min(newInterval[0],intervals[i][0])
                max_val = max(newInterval[1],intervals[i][1])
                i+=1
                while i<len(intervals) and intervals[i][0]<=max_val:
                    max_val = max(max_val,intervals[i][1])
                    i+=1

                lst.append([min_val,max_val])
                inserted=True
        if not inserted :
            lst.append(newInterval)
        return lst