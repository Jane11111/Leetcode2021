# -*- coding: utf-8 -*-
# @Time    : 2021-08-02 17:13
# @Author  : zxl
# @FileName: 004_6.py


class Solution:

    def findKthNum(self,nums1,nums2,k):

        if len(nums1) == 0:
            return nums2[k-1]
        if len(nums2) == 0:
            return nums1[k-1]

        i1 = 0
        j1 = len(nums1)-1
        i2 = 0
        j2 = len(nums2)-1

        while i1<=j1 and i2<=j2:

            m1 = (i1+j1)//2
            m2 = (i2+j2)//2

            if m1-i1+m2-i2+2<=k:
                if nums1[m1]<nums2[m2]:
                    k -= (m1 - i1 + 1)
                    i1=m1+1

                else:
                    k -= (m2 - i2 + 1)
                    i2 = m2+1
            else:
                if nums1[m1]>nums2[m2]:
                    j1 = m1-1
                else:
                    j2 = m2-1
        if i1>j1:
            return nums2[i2+k-1]
        if i2>j2:
            return nums1[i1+k-1]




    def findMedianSortedArrays(self, nums1 , nums2 ) -> float:



        m = len(nums1)
        n = len(nums2)

        if (m+n)%2 == 1:
            k = (m+n)//2+1
            num = self.findKthNum(nums1,nums2,k)
            return num
        else:
            k1 = (m+n)//2
            k2 = k1+1
            num1 = self.findKthNum(nums1,nums2,k1)
            num2 = self.findKthNum(nums1,nums2,k2)
            return (num1+num2)/2



obj = Solution()
nums1 = [ 2 ]
nums2 = [ ]
ans = obj.findMedianSortedArrays(nums1,nums2)
print(ans)