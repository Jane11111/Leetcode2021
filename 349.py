# -*- coding: utf-8 -*-
# @Time    : 2021-04-15 17:22
# @Author  : zxl
# @FileName: 349.py



class Solution:
    def intersection(self, nums1, nums2) :

        nums1.sort()
        nums2.sort()

        i = 0
        j = 0
        ans = []
        while i<len(nums1) and j<len(nums2):

            if nums1[i]<nums2[j]:
                while i<len(nums1) and nums1[i]<nums2[j]:
                    i+=1
            elif nums2[j]<nums1[i]:
                while j<len(nums2) and nums2[j]<nums1[i]:
                    j+=1

            while i+1<len(nums1) and nums1[i+1]==nums1[i]:
                i+=1

            while j+1<len(nums2) and nums2[j+1] == nums2[j]:
                j+=1

            if i<len(nums1) and j<len(nums2) and nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i+=1
                j+=1
        return ans

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
obj = Solution()
ans = obj.intersection(nums1,nums2)
print(ans)
