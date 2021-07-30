# -*- coding: utf-8 -*-
# @Time    : 2021-07-26 21:04
# @Author  : zxl
# @FileName: 154.py



class Solution:
    def findMin(self, nums ) -> int:

        l = 0
        h = len(nums)-1

        while l<h:
            m = (l+h)//2

            m1 = m+1
            while m1<=h and nums[m1]== nums[m]:
                m1+=1
            if m1>h:
                h = m
                continue

            if nums[m1]>nums[h]:
                l = m1
            else:
                if nums[m]<nums[m1]:
                    h = m
                else:
                    l = m1


        return nums[l]

obj = Solution()
nums =[1,1]
ans = obj.findMin(nums)
print(ans)