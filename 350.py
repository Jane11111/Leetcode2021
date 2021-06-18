# -*- coding: utf-8 -*-
# @Time    : 2021-06-18 15:47
# @Author  : zxl
# @FileName: 350.py



class Solution:
    def intersect(self, nums1 , nums2 ) :


        dic = {}
        for num in nums1:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1

        ans = []
        for num in nums2:
            if num in dic and dic[num]>0:
                ans.append(num)
                dic[num]-=1
        return ans



