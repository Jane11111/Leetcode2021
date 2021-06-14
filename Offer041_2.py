# -*- coding: utf-8 -*-
# @Time    : 2021-06-14 15:51
# @Author  : zxl
# @FileName: Offer041_2.py


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = [] # 小根堆，较大的一半 len(A) >= len(B)
        self.B = [] # 大根堆， 较小的一半

    def insertMinHeap(self,arr,num):
        arr.append(num)
        i = len(arr)-1
        while i>0:
            p = (i-1)//2
            if arr[p]>arr[i]:
                arr[i],arr[p] = arr[p],arr[i]
            else:
                break
            i = p
    def minHeapify(self,arr,i):
        idx = i
        l = 2*i+1
        r = 2*i+2
        if l<len(arr) and arr[l]<arr[idx]:
            idx = l
        if r<len(arr) and arr[r]<arr[idx]:
            idx = r
        if idx!= i:
            arr[i],arr[idx] = arr[idx],arr[i]
            self.minHeapify(arr,idx)
    def minPop(self,arr):
        if len(arr) == 1:
            return arr.pop()
        else:
            arr[0],arr[-1] = arr[-1],arr[0]
            v = arr.pop()
            self.minHeapify(arr,0)
            return v
    def maxPop(self,arr):
        if len(arr) == 1:
            return arr.pop()
        else:
            arr[0],arr[-1] = arr[-1],arr[0]
            v = arr.pop()
            self.maxHeapify(arr,0)
            return v

    def maxHeapify(self,arr,i):
        idx = i
        l = 2*i+1
        r = 2*i+2
        if l<len(arr) and arr[l]>arr[idx]:
            idx = l
        if r<len(arr) and arr[r]>arr[idx]:
            idx = r
        if idx!= i:
            arr[i],arr[idx] = arr[idx],arr[i]
            self.maxHeapify(arr,idx)

    def insertMaxHeap(self,arr,num):

        arr.append(num)
        i = len(arr) - 1
        while i > 0:
            p = (i - 1) // 2
            if arr[p] < arr[i]:
                arr[i], arr[p] = arr[p], arr[i]
            else:
                break
            i = p


    def addNum(self, num: int) -> None:

        if len(self.A) == len(self.B):

            self.insertMaxHeap(self.B,num)
            v = self.maxPop(self.B)
            self.insertMinHeap(self.A,v)
        else:
            self.insertMinHeap(self.A,num)
            v = self.minPop(self.A)
            self.insertMaxHeap(self.B,v)



    def findMedian(self) -> float:

        if len(self.A) == len(self.B):
            return (self.A[0]+self.B[0])/2
        else:
            return self.A[0]



