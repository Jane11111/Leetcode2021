# -*- coding: utf-8 -*-
# @Time    : 2021-05-10 20:53
# @Author  : zxl
# @FileName: 377_2.py


class Solution:

    def combinationSum4(self, nums, target):


        dp = [0 for i in range(target+1)]

        dp[0] = 1

        nums.sort()
        for i in range(1,target+1):
            for num in nums:
                if i-num<0:
                    break
                dp[i] += dp[i-num]
        return dp[target]

obj = Solution()
nums = [1,2,3]
target = 4
ans = obj.combinationSum4(nums,target)
print(ans)