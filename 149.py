# -*- coding: utf-8 -*-
# @Time    : 2021-06-29 11:34
# @Author  : zxl
# @FileName: 149.py

class Solution:

    def count(self,k,x,y,points):
        count = 0

        for i,j in points:
            if i == x and j == y:
                continue
            if i == x :
                if k == float('inf'):
                    count+=1
            else:
                if (j-y)/(i-x) == k:
                    count+=1
        return count+1



    def maxPoints(self, points ) -> int:

        if len(points)== 1:
            return 1

        ans = 0
        n = len(points)

        for i in range(n):
            for j in range(i+1,n):
                if points[i][0] == points[j][0]:
                    k = float('inf')
                else:
                    k = (points[j][1]-points[i][1])/(points[j][0]-points[i][0])
                count = self.count(k,points[i][0],points[i][1],points)
                ans = max(ans,count)
        return ans





