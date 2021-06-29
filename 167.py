# -*- coding: utf-8 -*-
# @Time    : 2021-06-29 15:19
# @Author  : zxl
# @FileName: 167.py

class Solution:
    def twoSum(self, numbers , target: int) :

        i = 0
        j = len(numbers)-1

        while i<j:
            n1 = numbers[i]
            n2 = numbers[j]
            if n1+n2 == target:
                return [i+1,j+1]
            if n1+n2<target:
                i+=1
            else:
                j-=1

        return []


