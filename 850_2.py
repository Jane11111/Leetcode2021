# -*- coding: utf-8 -*-
# @Time    : 2021-08-22 16:02
# @Author  : zxl
# @FileName: 850_2.py


class Solution:

    def calArea(self,width,intervals):
        intervals.sort()

        area = 0

        i = 0

        while i<len(intervals):

            max_height = intervals[i][1]
            j= i+1
            while j<len(intervals) and intervals[j][0]<=max_height:
                max_height = max(max_height,intervals[j][1])
                j+=1
            area += width*(max_height-intervals[i][0])

            i = j
        return area





    def rectangleArea(self, rectangles ) -> int:


        lst = []

        visited = {}
        for i in range(len(rectangles)):

            x1,y1,x2,y2 = rectangles[i]
            if x1 not in visited:
                lst.append(x1)
                visited[x1] = True
            if x2 not in visited:
                lst.append(x2)
                visited[x2] = True



        lst.sort()
        area = 0
        for i in range(len(lst)-1):

            x1 = lst[i]
            x2 = lst[i+1]

            intervals = []

            for j in range(len(rectangles)):

                if rectangles[j][0]<= x1 and rectangles[j][2]>=x2:
                    intervals.append([rectangles[j][1],rectangles[j][3]])


            cur_area = self.calArea(x2-x1,intervals)
            area += cur_area
            area = area%(10 ** 9 + 7)
        return area


