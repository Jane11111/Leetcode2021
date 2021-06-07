# -*- coding: utf-8 -*-
# @Time    : 2021-06-04 15:47
# @Author  : zxl
# @FileName: 075_4.py





class Solution:
    def sortColors(self, nums ) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        p0 = 0
        p1 = 0
        for num in nums:
            if num == 0:
                p1+=1


        i = 0
        while i<len(nums):


            num = nums[i]
            if num>3:
                i+=1
                continue

            if num == 0:
                if i == p0:
                    i+=1
                    p0+=1
                else:
                    nums[i],nums[p0] = nums[p0],nums[i]
                    nums[p0]+=3
                    p0+=1
            elif num == 1:
                if i == p1:
                    i+=1
                    p1+=1
                else:
                    nums[i],nums[p1] = nums[p1],nums[i]
                    nums[p1]+=3
                    p1+=1

            else:
                i+=1
        for i in range(len(nums)):
            nums[i] %=3

obj = Solution()
nums = [2,0,2,1,1,0]
ans = obj.sortColors(nums)
print(nums)