# -*- coding: utf-8 -*-
# @Time    : 2021-04-17 19:32
# @Author  : zxl
# @FileName: 053.py


class Solution:
    def maxSubArray(self, nums) :

        if len(nums) == 1:
            return nums[0]

        i = 0
        ans = float('-inf')
        while i<len(nums) and nums[i]<=0:
            ans = max(ans,nums[i])
            i+=1

        if i < len(nums):
            ans = nums[i]
        i+=1

        max_val = ans
        while i<len(nums):
            if nums[i]>=0:
                ans+=nums[i]
                max_val = max(ans, max_val)

                i+=1
            else:

                max_val = max(ans, max_val)

                neg_val = nums[i]
                i+=1
                while i<len(nums) and nums[i]<=0:
                    neg_val += nums[i]
                    i+=1

                if neg_val + ans > 0:
                    ans += neg_val
                else:
                    ans = 0

        return max_val

obj = Solution()
nums = [-2]
ans = obj.maxSubArray(nums)
print(ans)



