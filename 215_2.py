# -*- coding: utf-8 -*-
# @Time    : 2021-05-08 14:00
# @Author  : zxl
# @FileName: 215_2.py


class Solution:


    def buildHeap(self,nums):

        for i in range(len(nums)//2,-1,-1):
            self.minHeapify(nums,i)

    def minHeapify(self,nums,i):

        largest_idx = i
        if 2*i+1<len(nums) and nums[largest_idx]>nums[2*i+1]:
            largest_idx = 2*i+1
        if 2*i+2<len(nums) and nums[largest_idx]>nums[2*i+2]:
            largest_idx = 2*i+2

        if largest_idx != i:
            nums[i],nums[largest_idx] = nums[largest_idx],nums[i]
            self.minHeapify(nums,largest_idx)

    def findKthLargest(self, nums , k ) :


        my_heap = nums[:k]
        self.buildHeap(my_heap)

        for i in range(k,len(nums)):
            if nums[i]>my_heap[0]:
                my_heap[0] = nums[i]
                self.minHeapify(my_heap,0)
        return my_heap[0]
