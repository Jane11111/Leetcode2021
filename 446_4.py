# -*- coding: utf-8 -*-
# @Time    : 2021-07-04 12:44
# @Author  : zxl
# @FileName: 446_4.py



class Solution:

    def numberOfArithmeticSlices(self, nums) -> int:

        n = len(nums)

        dp = {n-1:{}}
        ans = 0
        for i in range(n-2,-1,-1):
            dp[i] = {}
            for j in range(n-1,i,-1):

                diff = nums[j]-nums[i]
                if diff not in dp[i]:
                    dp[i][diff] = 0

                v = 0
                if diff in dp[j]:
                    v = dp[j][diff]
                dp[i][diff] += 1+v
                ans+=v
        return ans


obj = Solution()
nums = [2, 4, 6, 8, 10]


ans = obj.numberOfArithmeticSlices(nums)
print(ans)
