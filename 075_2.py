# -*- coding: utf-8 -*-
# @Time    : 2021-03-10 18:50
# @Author  : zxl
# @FileName: 075_2.py



class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        i = 0
        count = 0
        while i<len(nums) and count<len(nums):
            count+=1
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(0,0)

                i+=1
            elif nums[i] == 2:
                nums.insert(len(nums),2)
                nums.pop(i)
            else:
                i+=1
obj = Solution()
nums = [2,0,2,1,1,0]
ans = obj.sortColors(nums)
print(nums)