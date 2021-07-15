# -*- coding: utf-8 -*-
# @Time    : 2021-07-13 17:00
# @Author  : zxl
# @FileName: 377_6.py



class Solution:
    def combinationSum4(self, nums, target: int) -> int:

        if target == 0:
            return 0


        dp = [0 for i in range(target+1)]
        dp[0] = 1

        for val in range(1,target+1):

            for num in nums:
                if val-num>=0:
                    dp[val]+=dp[val-num]
        return dp[target]
