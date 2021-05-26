# -*- coding: utf-8 -*-
# @Time    : 2021-05-24 22:43
# @Author  : zxl
# @FileName: 041_2.py


class Solution:
    def firstMissingPositive(self, nums ) -> int:

        i = 0
        nums.append(0)
        n = len(nums)
        while i<n:

            num = nums[i]
            if num>=0 and num<n and nums[num] != num:
                tmp = nums[num]
                nums[num] = num
                nums[i] = tmp
            else:
                i+=1

            # if num>=len(nums) or num == i or num<0:
            #     i+=1
            # else:
            #     tmp = nums[num]
            #     if tmp == num:
            #         i+=1
            #         continue
            #     nums[num] = num
            #     nums[i] = tmp
        for i in range(1,n):
            if nums[i]!=i:
                return i
        return n