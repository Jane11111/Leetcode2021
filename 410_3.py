# -*- coding: utf-8 -*-
# @Time    : 2021-06-16 20:21
# @Author  : zxl
# @FileName: 410_3.py

# O(Nlog(sum-max))

class Solution:

    def check(self,nums,max_val,m):

        cnt = 1
        sum_val = 0
        for num in nums:
            sum_val+=num
            if sum_val>max_val:
                cnt+=1
                sum_val = num
        return cnt<=m



    def splitArray(self, nums, m: int) -> int:


        right = 0
        left = 0
        for num in nums:
            if num>left:
                left = num
            right += num


        while left<right:
            mid = (left+right)//2

            if self.check(nums,mid,m):
                right = mid
            else:
                left = mid+1
        return left



