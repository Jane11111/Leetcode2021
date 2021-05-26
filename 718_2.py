# -*- coding: utf-8 -*-
# @Time    : 2021-05-24 15:51
# @Author  : zxl
# @FileName: 718_2.py




class Solution:
    def findLength(self, nums1 , nums2 ) -> int:
        dic = {}
        for i in range(len(nums2)):
            if nums2[i] not in dic:
                dic[nums2[i]] = []
            dic[nums2[i]].append(i)

        i = 0
        ans = 0
        while i<len(nums1):
            if nums1[i] in dic:
                for idx in dic[nums1[i]]:
                    j = 1
                    while j+i<len(nums1) and j+idx<len(nums2):
                        if  nums2[j+idx]!= nums1[i+j]:
                            break
                        j+=1
                    ans = max(ans,j )
            i+=1
        return ans




