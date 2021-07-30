# -*- coding: utf-8 -*-
# @Time    : 2021-07-19 13:39
# @Author  : zxl
# @FileName: 327_3.py


class Solution:
    def countRangeSum(self, nums , lower: int, upper: int) -> int:

        lst = [0]
        sum_val = 0
        count = 0
        for num in nums:
            sum_val+=num
            for i in range(len(lst)):
                if sum_val-lst[i]>=lower and sum_val-lst[i]<=upper:
                    count+=1
            lst.append(sum_val)
        return count

