# -*- coding: utf-8 -*-
# @Time    : 2021-05-10 14:56
# @Author  : zxl
# @FileName: 1288.py


class Solution:
    def removeCoveredIntervals(self, intervals ) :

        for i in range(len(intervals)):
            intervals[i][1] = -intervals[i][1]

        intervals.sort()
        for i in range(len(intervals)):
            intervals[i][1] = -intervals[i][1]

        count =0
        i = 0
        j = 1
        while j<len(intervals):
            if intervals[j][0]>=intervals[i][0] and intervals[j][1] <=intervals[i][1]:
                count +=1
            if intervals[j][1]>=intervals[i][1]:
                i = j
                j = i+1
            else:
                j+=1
        return len(intervals)-count
obj = Solution()
intervals = [[1,4],[3,6],[2,8]]
ans = obj.removeCoveredIntervals(intervals)
print(ans)







