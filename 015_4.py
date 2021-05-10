# -*- coding: utf-8 -*-
# @Time    : 2021-05-08 21:35
# @Author  : zxl
# @FileName: 015_4.py



class Solution:
    def threeSum(self, nums ) :

        nums.sort()

        ans = []

        i=0

        while i<len(nums):

            num = nums[i]

            p = i+1
            q = len(nums)-1
            while p<q:
                if nums[p]+nums[q]>-num:
                    q-=1
                elif nums[p]+nums[q] <-num:
                    p+=1
                else:
                    ans.append([num,nums[p],nums[q]])
                    p+=1
                    while p<len(nums) and nums[p]==nums[p-1]:
                        p+=1
            i+=1
            while i<len(nums) and nums[i]==nums[i-1]:
                i+=1
        return ans

obj = Solution()
nums = [-1,0,1,2,-1,-4]
ans = obj.threeSum(nums)
print(ans)

