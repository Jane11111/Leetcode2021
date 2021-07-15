# -*- coding: utf-8 -*-
# @Time    : 2021-07-13 12:24
# @Author  : zxl
# @FileName: 045_1.py


class Solution:
    def jump(self, nums ) -> int:

        if len(nums) == 1:
            return 0

        i = 0
        ans = 1
        max_len = nums[0]

        while i<len(nums):

            if max_len>=len(nums)-1:
                break

            next_start = max_len+1
            for j in range(max_len+1):

                max_len = max(max_len,j+nums[j])
            ans += 1
            i = next_start
        return ans



