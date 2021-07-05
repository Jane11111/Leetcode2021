# -*- coding: utf-8 -*-
# @Time    : 2021-07-04 11:48
# @Author  : zxl
# @FileName: 446_2.py



import numpy as np
class Solution:

    def numberOfArithmeticSlices(self, nums) -> int:




        n = len(nums)

        dic = {}
        for i in range(n):
            if nums[i] not in dic:
                dic[nums[i]] = []
            dic[nums[i]].append(i)

        dp = []
        for i in range(n):
            dp.append([0 for j in range(n)])
        ans = 0

        for i in range(n-1,-1,-1):
            for j in range(n-1,i,-1):

                diff = nums[j]-nums[i]

                next_num = nums[j]+diff
                v = 0

                if next_num in dic:
                    for k in range(len(dic[next_num])-1,-1,-1):
                        idx = dic[next_num][k]
                        if idx<=j:
                            break
                        v+= 1+dp[j][idx]

                dp[i][j] = v
                ans += v
        return ans

obj = Solution()
nums = [5,5,5,5,5]

ans = obj.numberOfArithmeticSlices(nums)
print(ans)

