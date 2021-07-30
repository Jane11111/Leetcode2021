# -*- coding: utf-8 -*-
# @Time    : 2021-07-26 10:10
# @Author  : zxl
# @FileName: 850.py


class Solution:

    def mergeRec(self,x,lst):

        lst.sort()
        area = 0

        i = 0
        while i<len(lst):
            min_y = lst[i][0]
            max_y = lst[i][1]
            j = i+1
            while j<len(lst) and lst[j][0]<=max_y:
                max_y = max(lst[j][1],max_y)
                j+=1
            area += x*(max_y-min_y) # 一个区间

            i=j
        return area%(10**9 + 7)



    def rectangleArea(self, rectangles ) -> int:


        lst = []
        for x1,y1,x2,y2 in rectangles:
            if x1 not in lst:
                lst.append(x1)
            if x2 not in lst:
                lst.append(x2)

        lst.sort()
        area = 0

        for i in range(len(lst)-1):

            x1 = lst[i]
            x2 = lst[i+1]

            rec_lst = []

            for j in range(len(rectangles)):
                x3,y3,x4,y4 = rectangles[j]
                if x3<=x1 and x4>=x2:
                    rec_lst.append([y3,y4])
            cur_area = self.mergeRec(x2-x1,rec_lst)
            area += cur_area
            area = area%(10**9 + 7)
        return area




obj = Solution()
rectangles = [[0,0,1000000000,1000000000]]
ans = obj.rectangleArea(rectangles)
print(ans)


