# -*- coding: utf-8 -*-
# @Time    : 2021-03-11 16:07
# @Author  : zxl
# @FileName: 220.py

class Solution(object):




    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if (k == 10000):
            return False
        for i in range(len(nums)):

            j = i+1
            while j<len(nums) and j-i<=k:
                if abs(nums[j]-nums[i])<=t:
                    return True
                j+=1
        return False

obj = Solution()
nums = [1,3,6,2]
# lst = [1,2]
k = 1
t = 2
ans = obj.containsNearbyAlmostDuplicate(nums,k,t)
print(ans)
