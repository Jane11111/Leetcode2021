# -*- coding: utf-8 -*-
# @Time    : 2021-04-18 20:53
# @Author  : zxl
# @FileName: T003.py

import sys


import numpy as np
def solve(r1,x1,y1,x3,y3):

    dist = np.sqrt((x3-x1)**2+(y3-y1)**2)
    r2 = (dist+r1)/2

    if y1 == y3:
        y0 = y1
        if x3<=y1:
            x0 = x1+r1
        else:
            x0 = x1-r1
    else:
        k  = (x1-x3)/(y1-y3)
        y0 = np.sqrt(r1**2/(1+k**2))+y1
        x0 = x1+k*(y0-y1)
    x2 = (x0+x3)/2
    y2 = (y0+y3)/2
    return x2,y2,r2






if __name__ == "__main__":

    line = sys.stdin.readline().strip()
    values = list(map(float, line.split()))

    ans = solve(values[0],values[1],values[2],values[3],values[4])
    print('%.10f %.10f %.10f' % (ans[0], ans[1], ans[2]))
