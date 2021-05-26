# -*- coding: utf-8 -*-
# @Time    : 2021-05-13 13:12
# @Author  : zxl
# @FileName: 088_3.py



class Solution:
    def merge(self, nums1 , m: int, nums2 , n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if n==0:
            return

        p = m+n-1
        i = m-1
        j = n-1
        while p>=0:
            if i>=0:
                n1 = nums1[i]
            else:
                n1 = float('-inf')
            if j>=0:
                n2 = nums2[j]
            else:
                n2 = float('-inf')
            if n1>=n2:
                nums1[p] = n1
                i-=1
            else:
                nums1[p] = n2
                j-=1
            p-=1
