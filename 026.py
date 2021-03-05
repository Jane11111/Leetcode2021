# -*- coding: utf-8 -*-
# @Time    : 2021-03-02 11:00
# @Author  : zxl
# @FileName: 026.py


class Solution(object):

    def swap(self,nums,i,j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        i = 0 # 遍历list
        p = 1 # 交换数字
        res = 1

        j = i+1
        while j< len(nums) and nums[i] == nums[j]: # 要限制j的范围，即第一个条件
            j += 1
        i = j


        while i < len(nums):

            res += 1


            j = i+1
            while j < len(nums) and nums[i] == nums[j]:
                j+=1
            self.swap(nums,p,i)

            p+=1
            i = j
        return res




obj = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
res = obj.removeDuplicates(nums)
print(res)
print(nums)