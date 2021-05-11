# -*- coding: utf-8 -*-
# @Time    : 2021-05-10 22:00
# @Author  : zxl
# @FileName: 078_3.py


class Solution:

    def subsets(self, nums ) :


        if len(nums) == 1:
            return [[],nums]

        ans = []

        lst = self.subsets(nums[1:])
        for sub_lst in lst:
            tmp = sub_lst[:]
            ans.append(tmp)
            sub_lst.insert(0,nums[0])
            ans.append(sub_lst)
        return ans