# -*- coding: utf-8 -*-
# @Time    : 2021-03-09 17:17
# @Author  : zxl
# @FileName: 452.py


class Solution(object):

    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        for i in range(len(points)): # 按照第二个元素从小到大排序
            tmp = points[i][0]
            points[i][0]= points[i][1]
            points[i][1] = tmp

        points.sort()

        for i in range(len(points)):
            tmp = points[i][0]
            points[i][0]= points[i][1]
            points[i][1] = tmp


        if len(points) == 0:
            return 0
        count = 0
        i = 0
        while i < len(points):
            bound = points[i][1]
            count += 1
            i += 1
            while i < len(points) and points[i][0] <= bound:

                i += 1

        return count

obj = Solution()
points = [[2,3],[2,3]]
res = obj.findMinArrowShots(points)
print(res)

