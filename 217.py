# -*- coding: utf-8 -*-
# @Time    : 2021-06-14 20:36
# @Author  : zxl
# @FileName: 217.py


class Solution:
    def containsDuplicate(self, nums ) -> bool:

        dic = {}
        for num in nums:
            if num in dic:
                return True
            dic[num] = True
        return False