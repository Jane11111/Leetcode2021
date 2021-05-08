# -*- coding: utf-8 -*-
# @Time    : 2021-05-08 14:17
# @Author  : zxl
# @FileName: 215_3.py

import random
class Solution:

    def partition(self,nums,i,j):

        if i>=j:
            return i

        num = nums[j]
        p = i-1
        for k in range(i,j):
            if nums[k]>num:
                nums[p+1],nums[k] = nums[k],nums[p+1]
                p+=1

        nums[p+1],nums[j] = nums[j],nums[p+1]
        return p+1




    def findKthLargest(self, nums, k):

        random.shuffle(nums)

        idx = -1
        lo = 0
        hi = len(nums)-1
        while idx!= k-1:

            idx = self.partition(nums,lo,hi)
            if idx<k-1:
                lo = idx+1
            else:
                hi = idx-1



        return nums[idx]


obj = Solution()
nums = [-1,2,0]
k = 1
ans = obj.findKthLargest(nums,k)
print(ans)

