# -*- coding: utf-8 -*-
# @Time    : 2021-05-10 11:07
# @Author  : zxl
# @FileName: 435_2.py


class Solution:
    def eraseOverlapIntervals(self, intervals ) -> int:

        if len(intervals) == 0:
            return 0


        intervals.sort()

        count = 0

        cur_end = intervals[0][1]
        for i in range(1,len(intervals)):
            x,y = intervals[i]
            if x<cur_end:
                count+=1
                cur_end = min(cur_end,y)
            else:
                cur_end = y
        return count

obj = Solution()
intervals = [ [1,2], [2,3] ]
ans = obj.eraseOverlapIntervals(intervals)
print(ans)

