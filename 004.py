# -*- coding: utf-8 -*-
# @Time    : 2021-02-14 16:08
# @Author  : zxl
# @FileName: 004.py
import numpy as np
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = 0
        j = 0

        arr = np.zeros(len(nums1)+len(nums2))
        while i < len(nums1) or j < len(nums2):
            if i == len(nums1):
                cur_val = nums2[j]
                j += 1
            elif j == len(nums2):
                cur_val = nums1[i]
                i += 1
            else:
                if nums1[i] <= nums2[j]:
                    cur_val = nums1[i]
                    i += 1
                else:
                    cur_val = nums2[j]
                    j += 1
            cur_idx = i + j - 1
            arr[cur_idx] = cur_val
        if (len(nums1)+len(nums2))%2 == 1:
            m = int((len(nums1)+len(nums2))/2)
            res = arr[m]
        else:
            m1 = int((len(nums1)+len(nums2))/2) -1
            m2 = int((len(nums1)+len(nums2))/2)
            res = (arr[m1]+arr[m2])/2
        return res



nums1 = [1,3]
nums2 = [2,4]

obj = Solution()
res = obj.findMedianSortedArrays(nums1,nums2)
print(res)