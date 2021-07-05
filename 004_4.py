# -*- coding: utf-8 -*-
# @Time    : 2021-07-04 17:06
# @Author  : zxl
# @FileName: 004_4.py



class Solution:

    def findMedianSortedArrays(self, nums1 , nums2 ) -> float:

        if len(nums1)>len(nums2): # 翻转一下是为了避免数组越界
            return self.findMedianSortedArrays(nums2,nums1)
        nums1.insert(0,float('-inf'))
        nums1.append(float('inf'))
        nums2.insert(0,float('-inf'))
        nums2.append(float('inf'))

        i = 0
        j = 0
        n1 = len(nums1)
        n2 = len(nums2)
        h = n1-1
        while i<h:


            m = (i+h)//2 # 对第一个序列做二分
            j = (n1 + n2 + 1) // 2 - m - 2
            # 找到一个i使得 nums[i]<=nums[j+1] && nums[j]<=nums[i+1]
            if nums1[m]<= nums2[j+1] and(m+1>h or nums2[j]<=nums1[m+1]):
                i = m
                break
            elif nums1[m]<=nums2[j+1]:
                i= m+1
            else:
                h = m

        if (n1+n2)%2 == 0:
            j = (n1+n2+1)//2 - i-2
            num1 = max(nums1[i],nums2[j])
            num2 = min(nums1[i+1],nums2[j+1])
            return (num1+num2)/2
        else:
            return max(nums1[i],nums2[j])


obj = Solution()
nums1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
nums2 = [99,100]
ans = obj.findMedianSortedArrays(nums1,nums2)
print(ans)

