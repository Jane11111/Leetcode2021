# -*- coding: utf-8 -*-
# @Time    : 2021-03-15 10:57
# @Author  : zxl
# @FileName: 198.py


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        if n==0:
            return 0

        a1 = [0 for i in range(n)] # not rob
        a2 = [0 for i in range(n)] # rob
        a2[0] = nums[0]
        for i in range(1,n):
            a1[i] = max(a1[i-1],a2[i-1])
            a2[i] = a1[i-1]+nums[i]

        return max(a1[n-1],a2[n-1])

obj = Solution()
nums = [2,7,9,3,1]
ans = obj.rob(nums)
print(ans)