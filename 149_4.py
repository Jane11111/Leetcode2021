# -*- coding: utf-8 -*-
# @Time    : 2021-08-20 21:31
# @Author  : zxl
# @FileName: 149_4.py

def gcd(a,b):
    if b>a:
        return gcd(b,a)

    while b:
        tmp = b
        b = a%b
        a = tmp
    return a

def findKB(x1,y1,x2,y2):

    if x1==x2:
        return float('inf'),0,x1
    if y1 == y2:
        return 0,0,y1

    n1 = y1-y2
    n2 = x1-x2
    neg = False
    if n1*n2<0:
        neg = True
    n1 = abs(n1)
    n2 = abs(n2)

    gcd_val = gcd(n1,n2)
    n1 = n1//gcd_val
    n2 = n2//gcd_val

    if neg:
        n2 = -n2
    b = n1/n2 * (0-x1)+y1

    return n1,n2,b





class Solution:
    def maxPoints(self, points ) -> int:
        if len(points) == 1:
            return 1

        dic = {}

        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1,len(points)):
                x2,y2 = points[j]
                n1,n2,b = findKB(x1,y1,x2,y2)

                if n1 not in dic:
                    dic[n1] = {}
                if n2 not in dic[n1]:
                    dic[n1][n2] = {}
                if b not in dic[n1][n2]:
                    dic[n1][n2][b] = []
                dic[n1][n2][b].append(i)
                dic[n1][n2][b].append(j)
        ans = 0
        for n1 in dic:
            for n2 in dic[n1]:
                for b in dic[n1][n2]:
                    ans = max(ans,len(set(dic[n1][n2][b])))
        return ans