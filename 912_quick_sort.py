# -*- coding: utf-8 -*-
# @Time    : 2021-05-15 10:34
# @Author  : zxl
# @FileName: 912.py

import  random


#时间复杂度 : O(nlogn) -> O(n^2)
#空间复杂度 : O(h)->O(n) 栈空间

class Solution:

    def partition(self,nums,i,j):

        x = nums[j]
        p = i-1
        for k in range(i,j):
            if nums[k]<x:
                p+=1
                nums[p],nums[k] = nums[k],nums[p]
        p+=1
        nums[p],nums[j] = nums[j],nums[p]
        return p



    def quickSort(self,nums,i,j):
        if i>=j:
            return
        r = self.partition(nums,i,j)
        self.quickSort(nums,i,r-1)
        self.quickSort(nums,r+1,j)


    def sortArray(self, nums ) :
        random.shuffle(nums)

        self.quickSort(nums,0,len(nums)-1)
        return nums


