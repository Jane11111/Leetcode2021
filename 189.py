# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 23:08
# @Author  : zxl
# @FileName: 189.py



class Solution:
    def rotate(self, nums , k ) :
        """
        Do not return anything, modify nums in-place instead.

        """

        n = len(nums)
        k = k%n

        if k==0:
            return

        count = 0
        i = 0
        j = (i+k)%n
        last_num = nums[i]
        while count < n:
            count+=1
            tmp = nums[j]
            nums[j] = last_num
            last_num = tmp
            if j == i:
                i+=1
                j = (i+k)%n
                last_num = nums[i]
            else:
                j=(j+k)%n
obj = Solution()
nums = [-1,-100,3,99]
k = 2
ans = obj.rotate(nums,k)
print(nums)






