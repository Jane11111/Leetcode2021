# -*- coding: utf-8 -*-
# @Time    : 2021-07-04 15:37
# @Author  : zxl
# @FileName: 004_3.py

class Solution:


    def findK(self,nums1,nums2,s1,e1,s2,e2,k):


        if s1>e1:
            return nums2[s2+k-1]
        if s2>e2:
            return nums1[s1+k-1]

        m1 = (s1+e1)//2
        m2 = (s2+e2)//2

        l1 = m1-s1+1
        l2 = m2-s2+1

        if l1+l2<=k:
            if nums1[m1]<=nums2[m2]:
                s1 = m1+1
                k -= (l1)
            else:
                s2 = m2+1
                k -= (l2)
        else:
            if nums1[m1]<=nums2[m2]:
                e2 = m2-1
            else:
                e1 = m1-1
        return self.findK(nums1,nums2,s1,e1,s2,e2,k)





    def findMedianSortedArrays(self, nums1 , nums2 ) -> float:


        n1 = len(nums1)
        n2 = len(nums2)

        if (n1+n2)%2 == 0:
            k1 = (n1+n2)//2
            k2 = k1+1
            num1 = self.findK(nums1,nums2,0,len(nums1)-1,0,len(nums2)-1,k1)
            num2 = self.findK(nums1,nums2,0,len(nums1)-1,0,len(nums2)-1,k2)
            return (num1+num2)/2
        else:

            k = (n1+n2+1)//2
            num = self.findK(nums1,nums2,0,len(nums1)-1,0,len(nums2)-1,k)
            return num


obj = Solution()
nums1 = [2]
nums2 = []
ans = obj.findMedianSortedArrays(nums1,nums2)
print(ans)

