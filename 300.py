# -*- coding: utf-8 -*-
# @Time    : 2021-03-17 16:34
# @Author  : zxl
# @FileName: 300.py


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        arr = [1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] >nums[j]:
                    arr[i] = max(arr[i],arr[j]+1)
        return max(arr)



obj = Solution()
nums =  [1,3,6,7,9,4,10,5,6]
ans = obj.lengthOfLIS(nums)
print(ans)




