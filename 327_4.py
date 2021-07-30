# -*- coding: utf-8 -*-
# @Time    : 2021-07-19 14:36
# @Author  : zxl
# @FileName: 327_4.py

import heapq

class Solution:

    def findLeft(self,lst,lower):

        l = 0
        r = len(lst)-1

        while l<r:
            m = (l+r)//2

            if lst[m]<lower:
                l = m+1
            else:
                r = m
        if lst[l]<lower:
            return -1
        return l

    def findRight(self,lst,upper):
        l = 0
        r = len(lst)-1
        while l<r:
            m = (l+r+1)//2
            if lst[m]>upper:
                r = m-1
            else:
                l = m
        if lst[l]>upper :
            return -1
        return l


    def countRangeSum(self, nums, lower: int, upper: int) -> int:

        sum_val = 0
        count = 0
        lst = [0]

        # heapq.heappush(lst,0)

        for i in range(len(nums)):
            sum_val+=nums[i]

            l = sum_val - upper
            r = sum_val - lower

            lidx = self.findLeft(lst,l)
            ridx = self.findRight(lst,r)
            if lidx!=-1 and ridx!=-1:
                count+= ridx-lidx+1

            idx = self.findRight(lst,sum_val)
            if idx == -1:
                lst.insert(0,sum_val)
            else:
                if idx == len(lst)-1:
                    lst.append(sum_val)
                else:
                    lst.insert(idx+1,sum_val)

        return count

obj = Solution()
nums =  [0]
lower = 0
upper = 0
ans = obj.countRangeSum(nums,lower,upper)
print(ans)


