# -*- coding: utf-8 -*-
# @Time    : 2021-03-09 22:33
# @Author  : zxl
# @FileName: 046.py


class Solution(object):
    def recursivePermute(self,nums):

        if len(nums) <= 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            v = nums[i]
            tmp = nums.copy()
            tmp.pop(i)
            lst = self.recursivePermute(tmp)
            for item in lst:
                item.insert(0,v)
                res.append(item)
        return res


    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = self.recursivePermute(nums)
        return res

obj = Solution()
nums = [1,2,3]
res = obj.permute(nums)
print(res)



