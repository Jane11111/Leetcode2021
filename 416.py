# -*- coding: utf-8 -*-
# @Time    : 2021-06-15 10:26
# @Author  : zxl
# @FileName: 416.py



class Solution:
    def canPartition(self, nums ) -> bool:




        target = int(sum(nums)/2)
        if target != sum(nums)/2:
            return False

        dp = []
        for i in range(len(nums)):
            dp.append([0 for j in range(target+1)])
        for i in range(len(nums)):
            dp[i][0] = 1

        for i in range(len(nums)):
            for j in range(1,target+1):
                dp[i][j]= dp[i-1][j]
                if nums[i]<=j:
                    dp[i][j]+=dp[i-1][j-nums[i]]
        return dp[len(nums)-1][target]>0


obj = Solution()
nums = [1,5,10,6]
ans = obj.canPartition(nums)
print(ans)



