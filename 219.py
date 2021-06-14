# -*- coding: utf-8 -*-
# @Time    : 2021-06-14 17:59
# @Author  : zxl
# @FileName: 219.py


class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:

        dic = {}

        for i in range(len(nums)):
            num = nums[i]

            if num in dic and dic[num] >0:
                return True
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] +=1
            if i-k>=0:
                dic[nums[i-k]]-=1
        return False





