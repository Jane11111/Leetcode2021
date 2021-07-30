# -*- coding: utf-8 -*-
# @Time    : 2021-07-29 20:09
# @Author  : zxl
# @FileName: 360_1.py

import sys

def solve(s,dic):


    if s in dic:
        return dic[s][1]

    f = True
    for i in range(len(s)):
        if s[i] == 'a' and i+1<len(s) and s[i+1] == 'b': #第一次这么变换
            f = False
            break
    if f:
        dic[s] = [0,0]
        return 0

    x = float('inf')
    y = float('inf')

    for i in range(len(s)):
        if s[i] == 'a' and i+1<len(s) and s[i+1] == 'b': #第一次这么变换
            news = s[:i]+'bba'+s[i+2:]
            cur_count = solve(news,dic)+1
            # count = min(count,(cur_count+1) )
            a = cur_count//1000000007
            b = cur_count%1000000007
            if a<x or (a==x and b<y):
                x = a
                y = b


    dic[s] = [x,y]
    return y

if __name__ == '__main__':

    s = sys.stdin.readline().strip()
    num = solve(s,{})
    print(num%1000000007)


