# -*- coding: utf-8 -*-
# @Time    : 2021-03-10 19:02
# @Author  : zxl
# @FileName: 209.py


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < target:
            return 0

        i = 0
        j = 0
        val = 0
        min_len = 100001

        while j<len(nums):
            val += nums[j]

            while val-nums[i] >= target:
                val-=nums[i]
                i+=1
            if val >= target:
                min_len = min(j-i+1,min_len)
            j+=1

        return min_len

obj = Solution()
target = 7
nums = [2,3,1,2,4,3]
min_len = obj.minSubArrayLen(target,nums)
print(min_len)

