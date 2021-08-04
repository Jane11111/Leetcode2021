# -*- coding: utf-8 -*-
# @Time    : 2021-08-02 20:05
# @Author  : zxl
# @FileName: 410_6.py


class Solution:

    def check(self,nums,max_val,m):

        sum_val = 0
        cnt = 1

        for num in nums:

            sum_val+=num
            if sum_val>max_val:
                cnt+=1
                sum_val = num
        return cnt<=m



    def splitArray(self, nums , m: int) -> int:



        left = float('-inf')
        right = 0

        for num in nums:
            left = max(left,num)
            right += num


        while left<right:

            mid = (left+right)//2

            if self.check(nums,mid,m):
                right = mid
            else:
                left = mid+1
        return left



