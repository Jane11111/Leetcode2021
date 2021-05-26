# -*- coding: utf-8 -*-
# @Time    : 2021-05-24 21:57
# @Author  : zxl
# @FileName: I1603.py



class Solution:
    def intersection(self, start1 , end1 , start2 , end2 ) :

        x1,y1 = start1[0],start1[1]
        x2,y2 = end1[0],end1[1]

        x3,y3 = start2[0],start2[1]
        x4,y4 = end2[0],end2[1]


        if x1!=x2 and x3!=x4:
            k1 = (y2-y1)/(x2-x1)
            k2 = (y4-y3)/(x4-x3)
            if k1!=k2: #斜率不同
                x0 = (k1*x1-k2*x3+y3-y1)/(k1-k2)
                y0 = k1*(x0-x1)+y1
                if (x0-x1)*(x0-x2)<=0 and (y0-y1)*(y0-y2)<=0 and (x0-x3)*(x0-x4)<=0 and (y0-y3)*(y0-y4)<=0:
                    return [x0,y0]
                else:
                    return []
            else: #斜率相同
                if y1-k1*x1 != y3-k2*x3: # 不是一条线
                    return []
                else: # 是一条线
                    if y3 >= min(y1, y2) and y3 <= max(y1, y2):
                        return [x3, y3]
                    elif y1 >= min(y3, y4) and y1 <= max(y3, y4):
                        return [x3, y1]
                    else:
                        return []
        elif x1!=x2:
            k1 = (y2 - y1) / (x2 - x1)
            x0 = x3
            y0 = y1+k1*(x0-x1)
            if (x0 - x1) * (x0 - x2) <= 0 and (y0 - y1) * (y0 - y2) <= 0 and (x0 - x3) * (x0 - x4) <= 0 and (
                    y0 - y3) * (y0 - y4) <= 0:
                return [x0, y0]
            else:
                return []
        elif x3!=x4:
            k2 = (y4 - y3) / (x4 - x3)
            x0 = x1
            y0 = y3+k2*(x0-x3)
            if (x0 - x1) * (x0 - x2) <= 0 and (y0 - y1) * (y0 - y2) <= 0 and (x0 - x3) * (x0 - x4) <= 0 and (
                    y0 - y3) * (y0 - y4) <= 0:
                return [x0, y0]
            else:
                return []
        else:
            if x1!= x3:
                return []
            elif y3>=min(y1,y2) and y3<=max(y1,y2):
                return [x3,y3]
            elif y1>=min(y3,y4) and y1<=max(y3,y4):
                return [x3,y1]
            else:
                return []