# -*- coding: utf-8 -*-
# @Time    : 2021-05-13 16:44
# @Author  : zxl
# @FileName: 209_2.py


class Solution:
    def minSubArrayLen(self, target: int, nums ) -> int:


        min_length = float('inf')

        i = 0
        sum_val = 0

        for j in range(len(nums)):
            sum_val+=nums[j]
            while sum_val-nums[i]>=target:

                sum_val -= nums[i]
                i += 1
            if sum_val>=target:
                min_length = min(min_length,j-i+1)
        if min_length == float('inf'):
            min_length = 0
        return min_length

obj = Solution()
target = 11
nums = [1,4,4]
ans = obj.minSubArrayLen(target,nums)
print(ans)



