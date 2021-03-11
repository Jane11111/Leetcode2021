# -*- coding: utf-8 -*-
# @Time    : 2021-03-10 19:34
# @Author  : zxl
# @FileName: 080.py

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 1
        while i<len(nums):

            if nums[i] != nums[i-1] :
                i+=1
            elif i+1<len(nums) and nums[i+1] == nums[i]:
                nums.pop(i)
            else:
                i+=1

obj = Solution()
nums = [0,0,1,1,1,1,2,3,3]
obj.removeDuplicates(nums)
print(nums)