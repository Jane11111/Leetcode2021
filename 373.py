# -*- coding: utf-8 -*-
# @Time    : 2021-04-08 10:47
# @Author  : zxl
# @FileName: 373.py


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):

        # nums1,nums2 = (nums2,nums1) if len(nums2)<len(nums1) else (nums1,nums2)

        arr = [0 for i in range(len(nums1))]

        ans = []

        while len(ans) < k:
            idx = -1
            min_val = float('inf')

            for i in range(len(arr)):
                if arr[i] >= len(nums2):
                    continue
                if nums1[i] + nums2[arr[i]] < min_val:
                    min_val = nums1[i] + nums2[arr[i]]
                    idx = i
            if idx == -1:
                break
            ans.append([nums1[idx], nums2[arr[idx]]])
            arr[idx] += 1
        return ans