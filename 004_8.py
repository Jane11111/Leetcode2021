# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 15:02
# @Author  : zxl
# @FileName: 004_8.py




class Solution:


    def findKthNum(self,nums1,nums2,k):

        if len(nums1) == 0:
            return nums2[k-1]
        if len(nums2) == 0:
            return nums1[k-1]

        m1 = (len(nums1)-1)//2
        m2 = (len(nums2)-1)//2

        if m1+1+m2+1<=k:
            if nums1[m1]<=nums2[m2]:
                nums1 = nums1[m1+1:]
                k-=(m1+1)
            else:
                nums2 = nums2[m2+1:]
                k-=(m2+1)
        else:
            if nums1[m1]>=nums2[m2]:
                nums1 = nums1[:m1]
            else:
                nums2 = nums2[:m2]
        return self.findKthNum(nums1,nums2,k)





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

nums1 = [2]
nums2 = [3,4]
obj = Solution()
ans = obj.findMedianSortedArrays(nums1,nums2)
print(ans)

