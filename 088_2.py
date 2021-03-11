# -*- coding: utf-8 -*-
# @Time    : 2021-03-10 22:30
# @Author  : zxl
# @FileName: 088_2.py


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        p = m+n-1
        m-=1
        n-=1
        while p>=0:
            if m<0:
                while n>=0:
                    nums1[p] = nums2[n]
                    p-=1
                    n-=1
            if n<0:
                return
            else:
                if nums1[m]>nums2[n]:
                    nums1[p]=nums1[m]
                    m-=1
                    p-=1
                else:
                    nums1[p] = nums2[n]
                    n-=1
                    p-=1


