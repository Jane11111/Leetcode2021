# -*- coding: utf-8 -*-
# @Time    : 2021-05-10 15:54
# @Author  : zxl
# @FileName: 312_2.py


class Solution:




    def maxCoins(self, nums ) :

        nums.insert(0,1)
        nums.append(1)

        n = len(nums)
        dp = []
        for i in range(n):
            dp.append([0 for j in range(n)])

        for l in range(3,n+1):
            for i in range(n):
                j = i+l-1
                if j>=n:
                    break
                for k in range(i+1,j):
                    dp[i][j] = max(dp[i][j],nums[i]*nums[j]*nums[k]+dp[i][k]+dp[k][j])
        return dp[0][-1]

obj = Solution()
nums = [3,1,5,8]
ans= obj.maxCoins(nums)
print(ans)