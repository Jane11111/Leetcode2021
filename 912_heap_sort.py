# -*- coding: utf-8 -*-
# @Time    : 2021-05-15 10:56
# @Author  : zxl
# @FileName: 912_heap_sort.py

# 时间复杂度 O(nlog(n))
#空间复杂度 O(1)

class Solution:

    def build_head(self,nums):

        for i in range(len(nums)//2,-1,-1):
            self.min_heapify(nums,i)


    def min_heapify(self,nums,i):
        lc = 2*i+1
        rc = 2*i+2
        idx = i
        if lc < len(nums) and nums[lc]<nums[idx]:
            idx = lc
        if rc< len(nums) and nums[rc] < nums[idx]:
            idx = rc
        if idx!=i:
            nums[i],nums[idx] = nums[idx],nums[i]
            self.min_heapify(nums,idx)


    def heap_sort(self,nums):

        self.build_head(nums)

        ans = []
        while len(nums)>0:
            ans.append(nums[0])
            v = nums.pop()
            if len(nums)>0:
                nums[0] = v
                self.min_heapify(nums,0)
        return ans




    def sortArray(self, nums ) :


        ans = self.heap_sort(nums)
        return ans

