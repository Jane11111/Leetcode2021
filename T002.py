# -*- coding: utf-8 -*-
# @Time    : 2021-04-18 20:19
# @Author  : zxl
# @FileName: T002.py


import sys


def solve(s,t,i,j):

    ans = len(t)-j

    while i < len(s) and len(s)-i +len(t)-j >ans:
        c1 = s[i]
        l1 = len(s)-i
        k = j
        while k<len(t) and t[k]<=c1 and l1+len(t)-k>ans:
            k+=1
        ans = max(ans,l1+len(t)-k)

        i+=1
    return ans

if __name__ == "__main__":
    # 读取第一行的n
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    for k in range(n):
        line = sys.stdin.readline()
        i,j = line.split()
        i = int(i)
        j = int(j)
        ans = solve(s,t,i-1,j-1)
        print(ans)



