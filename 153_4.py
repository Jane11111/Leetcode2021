# -*- coding: utf-8 -*-
# @Time    : 2021-07-26 21:22
# @Author  : zxl
# @FileName: 153_4.py


class Solution:
    def findMin(self, nums ) -> int:

        l = 0
        h = len(nums)-1

        while l<h:
            m = (l+h)//2

            if nums[m+1]>nums[h]:
                l = m+1
            else:
                if nums[m]<nums[m+1]:
                    h = m
                else:
                    l = m+1

        return nums[l]

obj = Solution()
nums = [11,13,15,17]
ans = obj.findMin(nums)
print(ans)