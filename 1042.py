# -*- coding: utf-8 -*-
# @Time    : 2021-03-31 15:02
# @Author  : zxl
# @FileName: 1042.py


class Solution(object):
    def gardenNoAdj(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """



obj = Solution()

n = 5
paths = [[3,4],[4,5],[3,2],[5,1],[1,3],[4,2]]
ans = obj.gardenNoAdj(n,paths)
print(ans)


