# -*- coding: utf-8 -*-
# @Time    : 2021-03-09 17:08
# @Author  : zxl
# @FileName: 435.py


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """


        for i in range(len(intervals)):
            tmp = intervals[i][0]
            intervals[i][0] = intervals[i][1]
            intervals[i][1] = tmp

        intervals.sort()

        for i in range(len(intervals)):
            tmp = intervals[i][0]
            intervals[i][0] = intervals[i][1]
            intervals[i][1] = tmp


        count = 0
        i = 0
        while i < len(intervals)-1:

            i+=1
            if intervals[i][0]>= intervals[i-1][1]:
                continue
            else:
                count += 1
                intervals[i][0] = intervals[i-1][0]
                intervals[i][1] = intervals[i-1][1]
        return count

obj = Solution()
intervals =  [ [1,2], [2,3] ]
res = obj.eraseOverlapIntervals(intervals)
print(res)

