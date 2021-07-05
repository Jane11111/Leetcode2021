# -*- coding: utf-8 -*-
# @Time    : 2021-07-04 15:16
# @Author  : zxl
# @FileName: 001_4.py

import numpy as np
class Solution:
    def twoSum(self, nums , target: int) :

        sorted_idx = np.array(nums).argsort()
        i = 0
        j = len(nums) - 1
        while i<j:
            if nums[sorted_idx[i]]+nums[sorted_idx[j]] == target:
                return [int(sorted_idx[i]),int(sorted_idx[j])]
            elif nums[sorted_idx[i]]+nums[sorted_idx[j]]<target:
                i+=1
            else:
                j-=1
obj = Solution()
nums = [2,7,11,15]
target = 9
ans = obj.twoSum(nums,target)
print(ans)
