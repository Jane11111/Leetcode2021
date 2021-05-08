# -*- coding: utf-8 -*-
# @Time    : 2021-05-08 13:31
# @Author  : zxl
# @FileName: 300_3.py


class Solution:
    def lengthOfLIS(self, nums )  :

        dp = []

        for num in nums:

            if len(dp) == 0 or num>dp[-1]:
                dp.append(num)
            else:

                lo = 0
                hi = len(dp)-1
                while lo<hi:
                    mid = (lo+hi)//2

                    if dp[mid]<num:
                        lo = mid+1
                    elif dp[mid] >num:
                        hi = mid
                    else:
                        lo = mid
                        hi = mid
                dp[lo] = min(num,dp[lo])
        return len(dp)

obj = Solution()
nums = [0,1,0,3,2,3]
ans = obj.lengthOfLIS(nums)
print(ans)