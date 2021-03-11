# -*- coding: utf-8 -*-
# @Time    : 2021-03-11 21:12
# @Author  : zxl
# @FileName: 033.py


class Solution(object):

    def bisearch(self,nums,p,q,target):
        if p>q:
            return -1
        if p==q:
            if nums[p] == target:
                return p
            else:
                return -1
        m = (p+q)//2
        if target <nums[m]:
            idx = self.bisearch(nums,p,m-1,target)
        elif target > nums[m]:
            idx = self.bisearch(nums,m+1,q,target)
        else:
            idx = m

        return idx



    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        i = 1
        while i<len(nums):
            if nums[i]<nums[i-1]:
                break
            i+=1

        idx1 = self.bisearch(nums,0,i-1,target)
        idx2 = self.bisearch(nums,i,len(nums)-1,target)
        if idx1!=-1:
            return idx1
        else:
            return idx2

obj = Solution()
nums = [1]
target = 0
ans = obj.search(nums,target)
print(ans)