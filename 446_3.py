# -*- coding: utf-8 -*-
# @Time    : 2021-07-04 12:06
# @Author  : zxl
# @FileName: 446_3.py


class Solution:

    def numberOfArithmeticSlices(self, nums) -> int:

        n = len(nums)

        dp = {0:{} }
        ans = 0

        for i in range(1,n):
            dp[i] = {}

            for j in range(i):

                diff = nums[i]-nums[j]
                if diff not in dp[i]:
                    dp[i][diff] = 0 # 初始化

                v = 0
                if diff  in dp[j]:
                    v = dp[j][diff]
                dp[i][diff]+= 1+v # 一定包含i
                ans+= v
        return ans


obj = Solution()
nums = [2,2,3,4]

ans = obj.numberOfArithmeticSlices(nums)
print(ans)





