# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 16:45
# @Author  : zxl
# @FileName: 373_2.py




class Solution:

    def maxHeapify(self,lst,idx):


        largest_idx = idx
        l = idx*2+1
        r = idx*2+2
        if l<len(lst) and sum(lst[l])>sum(lst[largest_idx]):
            largest_idx = l
        if r <len(lst) and sum(lst[r])>sum(lst[largest_idx]):
            largest_idx = r
        if largest_idx!=idx:
            lst[idx], lst[largest_idx] = lst[largest_idx],lst[idx]
            self.maxHeapify(lst,largest_idx)



    def insertMaxHeap(self,lst,x,y):

        lst.append([x,y])
        i = len(lst)-1

        while i>0:
            p = (i-1)//2
            if sum(lst[p]) < sum(lst[i]):
                lst[i],lst[p] = lst[p],lst[i]
            i = p




    def kSmallestPairs(self, nums1, nums2, k) :

        lst = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if len(lst)<k:
                    self.insertMaxHeap(lst,nums1[i],nums2[j])
                else:
                    if nums1[i]+nums2[j]<sum(lst[0]):
                        lst[0] = [nums1[i],nums2[j]]
                        self.maxHeapify(lst,0)
        ans = []

        while len(lst)>0:
            ans.insert(0,lst[0])
            lst[0] = lst[-1]
            lst.pop()
            self.maxHeapify(lst,0)
        return ans

