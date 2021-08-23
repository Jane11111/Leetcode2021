# -*- coding: utf-8 -*-
# @Time    : 2021-08-20 11:52
# @Author  : zxl
# @FileName: 149_3.py


def gcd(a,b):
    if b>a:
        return gcd(b,a)

    while b:
        tmp = b
        b = a%b
        a = tmp
    return a


def findK(x1,y1,x2,y2):

    if x1 == x2:
        return float('inf'),0
    if y1 == y2:
        return 0,0

    a = y2-y1
    b = x2-x1
    neg = False
    if a*b <0:
        neg = True
    a = abs(a)
    b = abs(b)

    k = gcd(a,b)

    a = a//k
    b = b//k
    if neg:
        b = -b

    return a,b





class Solution:
    def maxPoints(self, points ) -> int:
        if len(points) == 1:
            return 1

        dic = {}
        ans = 0

        for i in range(len(points)):
            x1,y1 = points[i]
            dic[i] = {}
            for j in range(i+1,len(points)):
                x2,y2 = points[j]

                a,b = findK(x1,y1,x2,y2)

                if a not in dic[i]:
                    dic[i][a] = {}
                if b not in dic[i][a]:
                    dic[i][a][b] = []
                dic[i][a][b].append(j)
        for i in dic:

            for a in dic[i]:
                for b in dic[i][a]:
                    ans = max(ans,len(dic[i][a][b])+1)
        return ans


