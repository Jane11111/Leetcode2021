# -*- coding: utf-8 -*-
# @Time    : 2021-03-15 22:47
# @Author  : zxl
# @FileName: 152_2.py


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_val = float('-inf')
        cur_min = 1
        cur_max = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                cur_min,cur_max = cur_max, cur_min
            cur_min = min(cur_min*nums[i],nums[i])
            cur_max = max(cur_max*nums[i],nums[i])
            max_val = max(max_val,cur_max)
        return max_val

obj = Solution()
nums = [-2,3,-4]
ans = obj.maxProduct(nums)
print(ans)


