# -*- coding: utf-8 -*-
# @Time    : 2021-05-08 13:15
# @Author  : zxl
# @FileName: 300_2.py


class Solution:
    def lengthOfLIS(self, nums )  :

        dp = [1 for i in range(len(nums))]

        for i in range(1,len(nums)):

            for j in range(i):

                if nums[j]<nums[i] :
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)


obj = Solution()
nums = [7,7,7,7,7,7,7]
ans = obj.lengthOfLIS(nums)
print(ans)