# -*- coding: utf-8 -*-
# @Time    : 2021-03-09 15:24
# @Author  : zxl
# @FileName: 605.py

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        for i in range(len(flowerbed)):
            if flowerbed[i] :
                continue

            if (i-1<0 or flowerbed[i-1] == 0) and (i+1>=len(flowerbed) or flowerbed[i+1] == 0):
                flowerbed[i]=1
                n-=1
                if n<=0:
                    return True
        if n<=0:
            return True
        return False