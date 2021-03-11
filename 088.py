# -*- coding: utf-8 -*-
# @Time    : 2021-03-10 22:22
# @Author  : zxl
# @FileName: 088.py

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while len(nums1)>m:
            nums1.pop(len(nums1)-1)

        i = 0
        j = 0

        while i<m or j<n:
            if i == m:
                while j<n:
                    nums1.insert(i,nums2[j])
                    i+=1
                    j+=1
            if j == n:
                i = m
            else:
                if nums1[i]<=nums2[j]:
                    i+=1
                else:
                    nums1.insert(i,nums2[j])
                    i+=1
                    m+=1
                    j+=1
obj = Solution()
nums1 = [1]
m = 1
nums2 = [ ]
n = 0
obj.merge(nums1,m,nums2,n)
print(nums1)

