# -*- coding: utf-8 -*-
# @Time    : 2021-06-23 11:41
# @Author  : zxl
# @FileName: 396.py


class Solution:
    def maxRotateFunction(self, nums ) -> int:


        if len(nums) == 0:
            return 0

        n = len(nums)
        post_arr = [num for num in nums]
        pre_arr = [num for num in nums]

        for i in range(n-2,-1,-1):
            post_arr[i]+=post_arr[i+1]
        for i in range(1,n):
            pre_arr[i] += pre_arr[i-1]

        sum_val = 0
        for i in range(n):
            sum_val += i*nums[i]

        ans = sum_val
        for i in range(1,n):
            sum_val = sum_val-post_arr[i]
            sum_val += (n-1)*nums[i-1]
            if i>1:
                sum_val -= pre_arr[i-2]
            ans = max(ans,sum_val)
            print(sum_val)
        return ans

obj = Solution()
nums = [4,3,2,6]
ans = obj.maxRotateFunction(nums)
# print(ans)











