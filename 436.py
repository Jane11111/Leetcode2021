# -*- coding: utf-8 -*-
# @Time    : 2021-05-10 11:59
# @Author  : zxl
# @FileName: 436.py

import numpy as np
class Solution:

    def bisearch(self,sorted_idx,nums,target):

        lo = 0
        hi = len(sorted_idx)-1
        while lo<=hi:

            m = (lo+hi)//2

            cur_idx = sorted_idx[m]
            if nums[cur_idx][0]<target:
                lo = m+1
            else:
                if m-1<0 or (nums[sorted_idx[m-1]][0]<target):
                    return int(sorted_idx[m])
                else:
                    hi = m-1


        return -1

    def findRightInterval(self, intervals ) :

        sorted_idx = np.argsort([i for i,j in intervals])

        arr = [-1 for i in range(len(intervals))]

        for i in range(len(intervals)):
            x,y = intervals[i]
            idx = self.bisearch(sorted_idx,intervals,y)
            arr[i] = idx
        return arr

obj = Solution()
intervals = [[1,4],[2,3],[3,4]]
ans = obj.findRightInterval(intervals)
print(ans)