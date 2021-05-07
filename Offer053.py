# -*- coding: utf-8 -*-
# @Time    : 2021-05-07 13:15
# @Author  : zxl
# @FileName: Offer053.py


class Solution:

    def biSearch(self,nums,target,i,j):
        if i>j:
            return 0
        if i==j:
            return int(nums[i]==target)
        m = (i+j)//2
        c1 = self.biSearch(nums,target,i,m)
        c2 = self.biSearch(nums,target,m+1,j)
        return c1+c2

    def search(self, nums , target ) :

        ans = self.biSearch(nums,target,0,len(nums)-1)
        return ans

obj = Solution()
nums = [5,7,7,8,8,10]
target = 8
ans = obj.search(nums,target)
print(ans)

