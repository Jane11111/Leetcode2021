# -*- coding: utf-8 -*-
# @Time    : 2021-06-03 22:10
# @Author  : zxl
# @FileName: 015_5.py

class Solution:
    def threeSum(self, nums ) :


        nums.sort()
        ans = []


        i = 0
        while i<len(nums):

            p = i+1
            q = len(nums)-1

            while p<q:

                if nums[p]+nums[q] == -nums[i]:
                    ans.append([nums[i],nums[p],nums[q]])

                    p+=1
                    while p<len(nums) and nums[p] == nums[p-1]:
                        p+=1
                elif nums[p]+nums[q]<-nums[i]:
                    p+=1
                else:
                    q-=1
            i+=1
            while i<len(nums) and nums[i]==nums[i-1]:
                i+=1
        return ans


nums = [-1,0,1,2,-1,-4]
obj = Solution()
ans = obj.threeSum(nums)
print(ans)
