# -*- coding: utf-8 -*-
# @Time    : 2021-03-04 17:28
# @Author  : zxl
# @FileName: 011.py




class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        res = 0
        while(i<j):
            res = max(res,(j-i)*min(height[i],height[j]))
            if height[i]>height[j]:
                j -= 1
            else:
                i += 1
        return res


obj = Solution()
height = [4,3,2,1,4]
res = obj.maxArea(height)
print(res)

