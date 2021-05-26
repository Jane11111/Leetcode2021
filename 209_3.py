# -*- coding: utf-8 -*-
# @Time    : 2021-05-13 17:03
# @Author  : zxl
# @FileName: 209_3.py


class Solution:

    def biSearch(self,nums,e,target):

        lo = 0
        hi = e
        while lo<hi:
            m = (lo+hi)//2 + (lo+hi)%2

            v = 0 if m==0 else nums[m-1]

            if nums[e]-v<target:
                hi=m-1
            else:
                lo=m

        return lo



    def minSubArrayLen(self, target: int, nums ) -> int:


        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        min_length = float('inf')
        for i in range(len(nums)):

            if nums[i]>=target:
                idx = self.biSearch(nums,i,target)
                min_length = min(min_length,(i-idx+1))
        if min_length == float('inf'):
            min_length = 0
        return min_length


