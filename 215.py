# -*- coding: utf-8 -*-
# @Time    : 2021-03-09 22:21
# @Author  : zxl
# @FileName: 215.py



class Solution(object):

    def mergeSort(self,nums):
        if len(nums)<=1:
            return nums

        m = len(nums)//2
        l = nums[:m]
        r = nums[m:]
        l = self.mergeSort(l)
        r = self.mergeSort(r)
        sorted_nums = self.merge(l,r)
        return sorted_nums



    def merge(self,l1,l2):
        lst = []
        i = 0
        j = 0
        while i<len(l1) or j<len(l2):
            if i==len(l1):
                while j<len(l2):
                    lst.append(l2[j])
                    j+=1
            elif j == len(l2):
                while i<len(l1):
                    lst.append(l1[i])
                    i+=1
            else:
                if l1[i]<l2[j]:
                    lst.append(l1[i])
                    i+=1
                else:
                    lst.append(l2[j])
                    j+=1
        return lst



    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums = self.mergeSort(nums)
        return nums[-k]

obj = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
res = obj.findKthLargest(nums,k)
print(res)