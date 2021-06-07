# -*- coding: utf-8 -*-
# @Time    : 2021-06-04 15:59
# @Author  : zxl
# @FileName: 075_6.py




class Solution:
    def sortColors(self, nums ) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums)-1

        i = 0
        while i<len(nums):
            if nums[i] == 0:
                nums[p0],nums[i] = nums[i],nums[p0]
                p0+=1
                i+=1

            elif nums[i] == 2:
                if i >p2:
                    i+=1
                    continue
                nums[i],nums[p2] = nums[p2],nums[i]
                p2-=1
                if nums[i] ==1:
                    i+=1
            else:
                i+=1


obj = Solution()
nums =  [2,1,2]
ans = obj.sortColors(nums)
print(nums)
