# -*- coding: utf-8 -*-
# @Time    : 2021-05-12 10:43
# @Author  : zxl
# @FileName: 001_3.py



class Solution:

    def twoSum(self, nums , target: int) :

        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic and nums[i]*2 == target:
                return [dic[nums[i]],i]
            dic[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in dic and dic[target-nums[i]] !=i:
                return [i,dic[target-nums[i]]]

nums = [3,2,4]
target = 6
obj = Solution()
ans = obj.twoSum(nums,target)

print(ans)