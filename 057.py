# -*- coding: utf-8 -*-
# @Time    : 2021-03-11 12:00
# @Author  : zxl
# @FileName: 057.py

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        ans = []
        i = 0
        while i<len(intervals):
            if newInterval == None or newInterval[0]>intervals[i][1]:
                ans.append(intervals[i])
                i+=1

            elif newInterval[1]<intervals[i][0]:
                ans.append(newInterval)
                newInterval = None
            else:
                left_bound = min(intervals[i][0],newInterval[0])
                right_bound = max(intervals[i][1],newInterval[1])
                i+=1
                while i<len(intervals) and intervals[i][0]<=right_bound:
                    right_bound = max(right_bound,intervals[i][1])
                    i+=1
                ans.append([left_bound,right_bound])
                newInterval=None

        if newInterval != None:
            ans.append(newInterval)
        return ans

obj = Solution()
intervals = [[1,5]]
newInterval = [0,0]
ans = obj.insert(intervals,newInterval)
print(ans)