# -*- coding: utf-8 -*-
# @Time    : 2021-07-14 13:53
# @Author  : zxl
# @FileName: 057_2.py


class Solution:
    def insert(self, intervals , newInterval ) :

        ans = []
        if len(intervals) == 0:
            return [newInterval]


        if newInterval[0]>intervals[-1][1]:
            intervals.append(newInterval)
            return intervals

        i = 0
        needed = True
        while i<len(intervals):
            if not needed:
                ans.append(intervals[i])
                i+=1
                continue

            if newInterval[1]<intervals[i][0]: # 要放到当前这个之前
                ans.append(newInterval)
                ans.append(intervals[i])
                i += 1
                needed = False
            elif (newInterval[0]>=intervals[i][0] and newInterval[0]<=intervals[i][1]) or\
                (intervals[i][0]>=newInterval[0] and intervals[i][0]<=newInterval[1]):
                min_val = min(intervals[i][0],newInterval[0])
                max_val = max(intervals[i][1],newInterval[1])
                i+=1
                while i<len(intervals) and intervals[i][0]<=max_val:
                    max_val = max(max_val,intervals[i][1])
                    i+=1
                ans.append([min_val,max_val])
                needed = False
            else:
                ans.append(intervals[i])
                i += 1

        return ans


obj = Solution()
intervals = [[1,5]]
newIntervals = [0,3]
ans = obj.insert(intervals,newIntervals)
print(ans)


