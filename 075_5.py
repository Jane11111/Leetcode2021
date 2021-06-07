# -*- coding: utf-8 -*-
# @Time    : 2021-06-04 15:54
# @Author  : zxl
# @FileName: 075_5.py




class Solution:
    def sortColors(self, nums ) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        p0 = 0
        p1 = 0

        for i in range(len(nums)):
            num = nums[i]

            if num == 1:
                nums[i],nums[p1] = nums[p1],nums[i]
                p1+=1
            elif num == 0:
                nums[i],nums[p0] = nums[p0],nums[i]
                if p0<p1:
                    nums[i],nums[p1] = nums[p1],nums[i]
                p0+=1
                p1+=1


obj = Solution()
nums = [2,0,1]
ans = obj.sortColors(nums)
print(nums)