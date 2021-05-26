# -*- coding: utf-8 -*-
# @Time    : 2021-05-12 10:10
# @Author  : zxl
# @FileName: 001.py


import numpy as np

class Solution:
    def twoSum(self, nums , target: int) :

        sorted_idx = np.argsort(nums)

        i = 0
        j = len(nums)-1
        while i<j:
            if nums[sorted_idx[i]]+nums[sorted_idx[j]] == target:
                return [int(sorted_idx[i]),int(sorted_idx[j])]
            elif nums[sorted_idx[i]] + nums[sorted_idx[j]] < target:
                i+=1
            else:
                j-=1


obj = Solution()
nums  = [2,1,3]
target = 3
ans = obj.twoSum(nums,target)
print(ans)
