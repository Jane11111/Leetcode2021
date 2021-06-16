# -*- coding: utf-8 -*-
# @Time    : 2021-06-16 14:57
# @Author  : zxl
# @FileName: 410_2.py



class Solution:

    def splitArray(self, nums, m: int) -> int:

        n = len(nums)
        dp = []
        for i in range(n):
            dp.append([0 for i in range(m+1)])


        for i in range(n):
            dp[i][1] = sum(nums[i:])

        for k in range(2,m+1):
            dp[n-k][k] = max(nums[n-k:])



        for k in range(2,m+1):
            for i in range(n-k):

                min_val = float('inf')
                sum_val = nums[i]
                for j in range(i+1,n-k+2):
                    if sum_val>=min_val:
                        break

                    max_val = max(dp[j][k-1],dp[i][1]-dp[j][1])
                    min_val = min(min_val,max_val)
                    sum_val+=nums[j]
                dp[i][k] = min_val

        return dp[0][m]


obj = Solution()
nums = [1,4,4]
m = 3
ans = obj.splitArray(nums,m)
print(ans)