# -*- coding: utf-8 -*-
# @Time    : 2021-05-12 10:18
# @Author  : zxl
# @FileName: 001_2.py



import numpy as np

class Solution:


    def biSearch(self,nums,sorted_idx,i,j,target):

        if i>j:
            return []
        if i==j:
            if target == nums[sorted_idx[i]]:
                return [sorted_idx[i]]
            else:
                return []

        m = (i+j)//2
        p = m
        while p-1>=i and nums[sorted_idx[p-1]] == nums[sorted_idx[p]]:
            p-=1
        q = m
        while q+1<=j and nums[sorted_idx[q+1]] == nums[sorted_idx[q]]:
            q+=1
        if nums[sorted_idx[m]] == target:
            return sorted_idx[p:q+1]
        elif nums[sorted_idx[m]]<target:
            return self.biSearch(nums,sorted_idx,q+1,j,target)
        else:
            return self.biSearch(nums,sorted_idx,i,p-1,target)


    def twoSum(self, nums , target: int) :

        sorted_idx = np.argsort(nums)



        for i in range(len(nums)):

            l = self.biSearch(nums,sorted_idx,0,len(nums)-1,target-nums[i])
            for j in range(len(l)):
                if i==l[j]:
                    continue
                else:
                    return [int(i),int(l[j])]


obj = Solution()
nums  = [-10,7,19,15]
target = 9
ans = obj.twoSum(nums,target)
print(ans)
