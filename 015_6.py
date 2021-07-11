# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 15:35
# @Author  : zxl
# @FileName: 015_6.py



class Solution:
    def threeSum(self, nums )  :

        nums.sort()
        ans = []
        i = 0
        while i <len(nums):
            if i-1>=0 and nums[i] == nums[i-1]:
                i+=1
                continue
            num = nums[i]
            l = i+1
            r = len(nums)-1
            while l<r:
                if nums[l]+nums[r]== -num:
                    ans.append([num,nums[l],nums[r]])
                    l+=1
                    while l<len(nums) and nums[l] == nums[l-1]:
                        l+=1
                elif nums[l]+nums[r]<-num:
                    l+=1
                    while l<len(nums) and nums[l] == nums[l-1]:
                        l+=1
                else:
                    r-=1
                    while r>= 0 and nums[r] == nums[r+1]:
                        r-=1
            i+=1
        return ans
