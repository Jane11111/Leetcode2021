# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 22:20
# @Author  : zxl
# @FileName: Offer003_2.py


class Solution:
    def findRepeatNumber(self, nums )  :

        n = len(nums)
        i = 0
        while i<n:
            if nums[i] == i:
                i+=1
                continue
            else:
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                else:
                    tmp = nums[i]
                    nums[i] = nums[tmp]
                    nums[tmp] = tmp

obj = Solution()
nums = [2, 3, 1, 0, 2, 5, 3]
ans = obj.findRepeatNumber(nums)
print(ans)