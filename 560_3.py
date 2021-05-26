# -*- coding: utf-8 -*-
# @Time    : 2021-05-18 15:55
# @Author  : zxl
# @FileName: 560_3.py



class Solution:
    def subarraySum(self, nums , k: int) -> int:


        dic  = {}
        ans = 0
        dic[0] = 1
        cur_sum = 0
        for num in nums:
            cur_sum += num
            if cur_sum - k in dic:
                ans+=dic[cur_sum-k]
            if cur_sum not in dic:
                dic[cur_sum] = 0
            dic[cur_sum] += 1
        return ans


