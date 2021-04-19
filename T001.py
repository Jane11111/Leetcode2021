# -*- coding: utf-8 -*-
# @Time    : 2021-04-18 20:17
# @Author  : zxl
# @FileName: T001.py


import sys

def solve(lst,w):
    for i in range(len(lst)):
        v = lst[i]
        if v+w in lst:
            return (v,v+w)
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
            print(-1)
        else:
            print(ans[0],' ',ans[1])
