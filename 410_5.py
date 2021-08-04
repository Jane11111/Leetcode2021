# -*- coding: utf-8 -*-
# @Time    : 2021-08-02 19:31
# @Author  : zxl
# @FileName: 410_5.py


class Solution:
    def splitArray(self, nums , m: int) -> int:


        n = len(nums)

        dp = []
        sum_val = 0
        for i in range(n):
            dp.append([float('inf') for j in range(m+1)])
            sum_val+=nums[i]
            dp[i][1] = sum_val


        for i in range(n):
            for j in range(2,min(i+2,m+1)):

                sum_val = nums[i]
                val = float('inf')
                for k in range(i-1,-1,-1): # 前k个数分成j-1段
                    cur_val = max(dp[k][j-1],sum_val)
                    sum_val += nums[k]
                    val = min(val,cur_val)
                dp[i][j] = val
        return int(dp[n-1][m])


obj = Solution()
nums = [1,4 ]
m = 2
ans = obj.splitArray(nums,m)
print(ans)

