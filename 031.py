# -*- coding: utf-8 -*-
# @Time    : 2021-04-16 14:04
# @Author  : zxl
# @FileName: 031.py


class Solution:
    def nextPermutation(self, nums )  :
        """
        Do not return anything, modify nums in-place instead.
        """

        i = len(nums)-2

        while i>=0 and nums[i]>=nums[i+1]:
            i-=1

        if i >-1:
            j = len(nums)-1
            while nums[j]<=nums[i]:
                j-=1
            nums[i],nums[j] = nums[j],nums[i]
        l = i+1
        r = len(nums)-1
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1

obj = Solution()
nums = [1]
obj.nextPermutation(nums)
print(nums)
