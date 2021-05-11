# -*- coding: utf-8 -*-
# @Time    : 2021-05-10 17:14
# @Author  : zxl
# @FileName: 452_2.py


class Solution:
    def findMinArrowShots(self, points ) :

        points.sort()
        if len(points) == 1:
            return 1

        count = 0
        i = 0
        while i<len(points):
            count +=1
            last_end= points[i][1]

            j=i+1
            while j<len(points) and points[j][0]<=last_end:
                last_end = min(last_end,points[j][1])
                j+=1
            i=j
        return count

obj = Solution()
points = [[2,3],[2,3]]
ans = obj.findMinArrowShots(points)
print(ans)



