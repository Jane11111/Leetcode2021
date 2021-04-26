# -*- coding: utf-8 -*-
# @Time    : 2021-04-25 10:27
# @Author  : zxl
# @FileName: M003.py

import sys

def solve(lst):

    i = 0
    j = len(lst)-1
    while i<len(lst) and lst[i]==i+1:
        i+=1
    while j>=0 and lst[j]==j+1:
        j-=1

    if i>=len(lst) or j<=0:
        return 0,0,0
    l =i
    while l+1<len(lst) and lst[l+1]-lst[l] == 1:
        l+=1
    r = j
    while r-1>=0 and lst[r]-lst[r-1] == 1:
        r-=1

    if r-l!=1:
        return -1,-1,-1

    return i+1,j+1,(l-i)+1

if __name__ == "__main__":
    # 读取第一行的n
    T = int(sys.stdin.readline().strip())

    for i in range(T):
        n = int(sys.stdin.readline().strip())
        line = sys.stdin.readline().strip()
        lst = list(map(int, line.split()))
        # print(lst)
        x,y,k = solve(lst)
        if x==0 and y==0 and k==0:
            print(0)
        elif x==-1 and y==-1 and k == -1:
            print(-1)
        else:
            print(x,y,k)
