# -*- coding: utf-8 -*-
# @Time    : 2021-03-11 22:34
# @Author  : zxl
# @FileName: 153_2.py

class Solution(object):


    def regularBiSearch(self,nums,i,j):

        if i>j:
            return 5001
        return nums[i]


    def biSearch(self,nums,i,j):
        if i == j:
            return nums[i]
        if i>j:
            return 5001
        m = (i+j)//2

        ans = nums[i]

        if nums[i] <= nums[m]:
            ans = min(ans,self.biSearch(nums,m+1,j))
        else:
            ans = min(ans,self.biSearch(nums,i+1,m))
        return ans






    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return self.biSearch(nums,0,len(nums)-1)

obj = Solution()
nums = [2,1]
ans = obj.findMin(nums)
print(ans)

