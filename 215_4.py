# -*- coding: utf-8 -*-
# @Time    : 2021-06-01 10:08
# @Author  : zxl
# @FileName: 215_4.py



class Solution:

    def buildHeap(self,arr):

        for i in range(len(arr)//2,-1,-1):
            self.minHeapify(arr,i)

    def minHeapify(self,arr,i):

        l = 2*i+1
        r = 2*i+2

        idx = i
        if l<len(arr) and arr[l]<arr[i]:
            idx = l
        if r<len(arr) and arr[r]<arr[idx]:
            idx = r
        if idx!=i:
            arr[i],arr[idx] = arr[idx],arr[i]
            self.minHeapify(arr,idx)


    def findKthLargest(self, nums , k: int) -> int:

        arr = nums[:k]
        self.buildHeap(arr)

        for i in range(k,len(nums),1):
            if nums[i]>arr[0]:
                arr[0] = nums[i]
                self.minHeapify(arr,0)
        return arr[0]

