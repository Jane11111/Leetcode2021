# -*- coding: utf-8 -*-
# @Time    : 2021-05-14 10:27
# @Author  : zxl
# @FileName: 287_4.py


class Solution:
    def findDuplicate(self, nums):



        slow = nums[0]
        fast = nums[nums[0]]

        while slow!=fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow!=fast:
            fast = nums[fast]
            slow = nums[slow]
        return slow

obj = Solution()
nums = [3,1,3,4,2]
ans = obj.findDuplicate(nums)
print(ans)
