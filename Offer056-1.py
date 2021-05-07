# -*- coding: utf-8 -*-
# @Time    : 2021-05-07 10:55
# @Author  : zxl
# @FileName: Offer56_1.py


class Solution:
    def singleNumbers(self, nums )  :

        x = 0
        for num in nums:
            x = x^num

        count = 0
        while x%2==0:
            x = x/2
            count+=1

        x = 0
        y = 0
        for num in nums:
            if (num>>count)%2:
                x^=num
            else:
                y^=num
        return [x,y]
