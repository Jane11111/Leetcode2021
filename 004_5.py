# -*- coding: utf-8 -*-
# @Time    : 2021-08-02 16:12
# @Author  : zxl
# @FileName: 004_5.py


class Solution:

    def findKthNum(self,nums1,nums2,k):



        if len(nums1) == 0:
            return nums2[k-1]
        if len(nums2) == 0:
            return nums1[k-1]

        if len(nums1)+len(nums2) == k:
            return max(nums1[-1],nums2[-1])

        m1 = (len(nums1)-1)//2
        m2 = (len(nums2)-1)//2

        if (m1+m2+2)<= k: # 小于等于的时候，完全可以把小的那一部分删除
            if nums1[m1]<=nums2[m2]:
                return self.findKthNum(nums1[m1+1:],nums2,k-(m1+1))
            else:
                return self.findKthNum(nums1,nums2[m2+1:],k-(m2+1))
        else: # 大于的时候，应该删大的那半边，注意：等于的时候不能删大的那半边
            if nums1[m1]<nums2[m2 ]:
                return self.findKthNum(nums1,nums2[:m2],k)
            else:
                return self.findKthNum(nums1[:m1],nums2,k)


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
nums1 = [1,3]
nums2 = [2]
ans = obj.findMedianSortedArrays(nums1,nums2)
print(ans)