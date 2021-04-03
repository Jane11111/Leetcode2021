# -*- coding: utf-8 -*-
# @Time    : 2021-03-21 15:13
# @Author  : zxl
# @FileName: 045.py


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp = [0]
        for i in range(1,len(nums)):
            min_val = float('inf')
            for j in range(i):
                if nums[j]+j>=i:
                    min_val = min(min_val,dp[j])
            dp.append(min_val+1)
        return dp[-1]

obj = Solution()
nums = [2,3,1,1,4]
print(obj.jump(nums))

