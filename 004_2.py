# -*- coding: utf-8 -*-
# @Time    : 2021-05-08 17:10
# @Author  : zxl
# @FileName: 004——2.py

import numpy as np

class Solution:

    def recursiveFind(self,arr1,arr2,k):
        if len(arr1) == 0:
            return arr2[k-1]
        if len(arr2) == 0:
            return arr1[k-1]

        m1 = len(arr1)//2
        m2 = len(arr2)//2

        if k<m1+m2+2:

            if arr1[m1] <= arr2[m2]:
                arr2 = arr2[:max(0,m2)]
            else:
                arr1 = arr1[:max(0,m1)]
        elif k==m1+m2+2:
            if arr1[m1]<=arr2[m2]:
                arr1 = arr1[m1+1:]
                k -=(m1+1)
            else:
                arr2 = arr2[m2+1:]
                k-=(m2+1)

        else:
            if arr1[m1] <= arr2[m2]:
                arr1 = arr1[m1+1:]
                k-=(m1+1)
            else:
                arr2 = arr2[m2+1:]
                k-=(m2+1)
        return self.recursiveFind(arr1,arr2,k)






    def findMedianSortedArrays(self, nums1, nums2) :


        m = len(nums1)
        n = len(nums2)
        if (m+n)%2:
            k_lst = [1+(m+n)//2]
        else:
            k_lst = [1+(m+n)//2,(m+n)//2]

        lst = []
        for k in k_lst:
            num = self.recursiveFind(nums1,nums2,k)
            lst.append(num)
        return np.mean(lst)

obj = Solution()
nums1 = [1,2]
nums2 = [3,4]
ans = obj.findMedianSortedArrays(nums1,nums2)
print(ans)




