# -*- coding: utf-8 -*-
# @Time    : 2021-08-02 19:18
# @Author  : zxl
# @FileName: 410_4.py


class Solution:
    def splitArray(self, nums , m: int) -> int:


        if len(nums)<m or len(nums)==0:
            return -1
        if len(nums) == m:
            return max(nums)
        if m == 1:
            return sum(nums)

        sum_val = 0
        ans = float('inf')
        for i in range(len(nums)):
            sum_val+=nums[i]

            if sum_val>ans:
                break

            tmp = self.splitArray(nums[i+1:],m-1)
            if tmp == -1:
                continue
            ans = min(ans,max(sum_val,tmp))


        return ans


