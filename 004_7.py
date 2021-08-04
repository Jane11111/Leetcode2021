# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 14:35
# @Author  : zxl
# @FileName: 004_7.py




class Solution:


    def findKthNum(self,nums1,nums2,k):

        s1 = 0
        e1 = len(nums1)-1
        s2 = 0
        e2 = len(nums2)-1

        while s1<=e1 and s2<=e2:

            m1 = (s1+e1)//2
            m2 = (s2+e2)//2

            if m1-s1+1+m2-s2+1<=k:
                if nums1[m1]<=nums2[m2]:
                    k-=(m1-s1+1)
                    s1 = m1+1

                else:
                    k-=(m2-s2+1)

                    s2 = m2+1
            else:
                if nums1[m1]>=nums2[m2]:
                    e1 = m1-1
                else:
                    e2 = m2-1
        if s1>e1:
            return nums2[s2+k-1]
        else:
            return nums1[s1+k-1]




    def findMedianSortedArrays(self, nums1 , nums2 ) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        if (n1+n2)%2 == 1:
            k = (n1+n2)//2+1
            return self.findKthNum(nums1,nums2,k)
        else:
            k1 = (n1+n2)//2
            k2 = k1+1
            num1 = self.findKthNum(nums1,nums2,k1)
            num2 = self.findKthNum(nums1,nums2,k2)
            return (num1+num2)/2

nums1 = [1]
nums2 = []
obj = Solution()
ans = obj.findMedianSortedArrays(nums1,nums2)
print(ans)