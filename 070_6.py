# -*- coding: utf-8 -*-
# @Time    : 2021-06-15 11:59
# @Author  : zxl
# @FileName: 070_6.py



class Solution:
    def climbStairs(self, n: int) -> int:



        nums = [1,2]

        dp = []
        for i in range(2):
            dp.append([0 for i in range(n+1)])
        # for i in range(len(nums)):
        #     dp[i][0] = 1
        dp[0][0] = 1

        for v in range(1,n+1):
            for i in range(len(nums)):
                if nums[i]>v:
                    continue
                for j in range(len(nums)):
                    dp[i][v]+= dp[j][v-nums[i]]
        ans = 0
        for i in range(len(nums)):
            ans+=dp[i][n]
        return ans


obj = Solution()
n = 10
ans = obj.climbStairs(n)
print(ans)