# -*- coding: utf-8 -*-
# @Time    : 2021-03-11 21:52
# @Author  : zxl
# @FileName: 034.py


class Solution(object):

    def bisearch(self,nums,target,i,j):
        if i>j:
            return [-1,-1]
        if i==j:
            if nums[i] == target:
                return [i,i]
            else:
                return [-1,-1]

        m = (i+j)//2
        if target <nums[m]:
            ans = self.bisearch(nums,target,i,m-1)
        elif target > nums[m]:
            ans = self.bisearch(nums,target,m+1,j)
        else:
            ans1 = self.bisearch(nums,target,i,m-1)
            ans2 = self.bisearch(nums,target,m+1,j)
            if ans1 == [-1,-1] and ans2 == [-1,-1]:
                ans = [m,m]
            elif ans1==[-1,-1]:
                ans = [m,ans2[1]]
            elif ans2 == [-1,-1]:
                ans = [ans1[0],m]
            else:
                ans = [ans1[0],ans2[1]]
        return ans



    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        ans = self.bisearch(nums,target,0,len(nums)-1)
        return ans
obj = Solution()
nums = [3,3,3]
target = 3
ans = obj.searchRange(nums,target)
print(ans)


