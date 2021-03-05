# -*- coding: utf-8 -*-
# @Time    : 2021-03-02 11:30
# @Author  : zxl
# @FileName: 027.py

class Solution(object):

    def swap(self,nums,i,j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        p = len(nums) - 1
        i = 0

        while i < p:

            if nums[i] == val:

                self.swap(nums, i, p)
                if nums[i] != val:
                    i+=1
                p-=1
            else:
                i+=1
        if nums[p] == val:
            return p
        return p+1


obj = Solution()
nums = [4,5]
val = 5

res = obj.removeElement(nums,val)
print(res)
print(nums)


