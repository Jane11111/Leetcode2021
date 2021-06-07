# -*- coding: utf-8 -*-
# @Time    : 2021-06-01 10:39
# @Author  : zxl
# @FileName: 215_5.py



class Solution:

    def partition(self,nums,s,e):
        if s==e:
            return s

        num = nums[e]
        p = s-1
        for i in range(s,e):
            if nums[i]>num:
                p+=1
                nums[p],nums[i] = nums[i],nums[p]

        nums[p+1],nums[e] = nums[e],nums[p+1]
        return p+1



    def findKthLargest(self, nums, k: int) -> int:



        lo = 0
        hi = len(nums)-1

        while lo<hi:
            idx = self.partition(nums,lo,hi)
            if idx<k-1:
                lo = idx+1
            elif idx>k-1:
                hi = idx-1
            else:
                lo = idx
                hi = idx
        return nums[lo]





