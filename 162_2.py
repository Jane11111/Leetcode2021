# -*- coding: utf-8 -*-
# @Time    : 2021-03-12 09:59
# @Author  : zxl
# @FileName: 162_2.py



class Solution(object):

    def biSearch(self,nums,i,j):
        if i==j:
            return i
        if i>j:
            return None

        m = (i+j)//2
        if nums[m]>nums[m+1]:
            ans = self.biSearch(nums,i,m)
        else:
            ans = self.biSearch(nums,m+1,j)
        return ans



    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = self.biSearch(nums,0,len(nums)-1)
        return ans

obj = Solution()
nums = [1,2,1,3,5,6,4]
ans= obj.findPeakElement(nums)
print(ans)


