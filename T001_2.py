# -*- coding: utf-8 -*-
# @Time    : 2021-04-18 21:37
# @Author  : zxl
# @FileName: T001_2.py


import sys

def solve(lst,w):
    i = 0
    j = 1
    while i<len(lst) and j<len(lst):
        if i==j:
            j+=1
        if lst[j]-lst[i] == w:
            return (lst[i],lst[j])
        elif lst[j]-lst[i]>w:
            i+=1
        else:
            j+=1
    return (-1,-1)

if __name__ == "__main__":
    # 读取第一行的n
    inline = sys.stdin.readline()
    n,m = inline.split()
    n = int(n)
    m = int(m)
    inline = sys.stdin.readline()
    lst = inline.split()
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    lst.sort()
    for i in range(m):
        w = int(sys.stdin.readline().strip())
        ans = solve(lst,w)
        if -1 in ans:
            print(-1,' ',-1)
        else:
            print(ans[0],' ',ans[1])
