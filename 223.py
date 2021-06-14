# -*- coding: utf-8 -*-
# @Time    : 2021-06-13 16:32
# @Author  : zxl
# @FileName: 223.py



class Solution:

    def findMiddle(self,x_lst ):
        min_x = min(x_lst)
        max_x = max(x_lst)
        i = -1
        j = -1
        for k in range(4):

            if x_lst[k] != min_x and x_lst[k] != max_x:
                if i == -1:
                    i = k
                else:
                    j = k
            else:
                if x_lst[k] == min_x:
                    min_x = max_x+1
                else:
                    max_x = max_x+1
        return abs(x_lst[i]-x_lst[j])
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        area = 0
        if not(bx1>=ax2 or bx2<=ax1 or by1>=ay2 or by2<=ay1):


            x_lst = [ax1,ax2,bx1,bx2]


            x = self.findMiddle(x_lst)

            y_lst = ([ay1,ay2,by1,by2])
            y = self.findMiddle(y_lst)
            area = x*y


        area1 = abs((ax1-ax2)*(ay1-ay2))
        area2 = abs((bx1-bx2)*(by1-by2))
        ans = area1+area2 - area

        return ans

obj = Solution()
ax1 = -2
ay1 = -2
ax2 = 2
ay2 = 2
bx1 = -2
by1 = -2
bx2 = 2
by2 = 2
ans = obj.computeArea(ax1,ay1,ax2,ay2,bx1,by1,bx2,by2)
print(ans)