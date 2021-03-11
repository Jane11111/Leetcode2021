# -*- coding: utf-8 -*-
# @Time    : 2021-03-11 15:09
# @Author  : zxl
# @FileName: 164.py

class Solution(object):

    def quick_sort(self,nums,p,q):
        if p>=q:
            return
        r = self.partition(nums,p,q)
        self.quick_sort(nums,p,r-1)
        self.quick_sort(nums,r+1,q)


    def partition(self,nums,p,q):

        i = p-1
        x= nums[q]
        for j in range(p,q,1):
            if nums[j]<x:
                i+=1
                nums[i],nums[j] = nums[j],nums[i]
        # nums[i+1],nums[q] = nums[q],nums[i+1]
        tmp = nums[i+1]
        nums[i+1] = nums[q]
        nums[q] = tmp
        return i+1


    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 2:
            return 0


        self.quick_sort(nums,0,len(nums)-1)

        max_val = 0
        for i in range(1,len(nums),1):
            max_val = max(max_val,nums[i]-nums[i-1])
        return max_val

obj = Solution()
nums = [1,2]

ans = obj.maximumGap(nums)
print(ans)

