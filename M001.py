# -*- coding: utf-8 -*-
# @Time    : 2021-04-25 10:51
# @Author  : zxl
# @FileName: M001.py

import sys

def solve(num,c):
    num %= (c*26)
    a = num//c
    a-=1

    b = num%c
    if a==-1 and b==0:
        a=25

    a += int(b>=1)
    if b == 0:
        b = c
    ans = str(chr(ord('A')+a))+str(b)
    return ans

if __name__ == "__main__":
    # 读取第一行的n
    inline = sys.stdin.readline().strip()
    n,c = inline.split()
    n = int(n)
    c = int(c)

    for i in range(n):
        num = int(sys.stdin.readline().strip())
        ans = solve(num,c)
        print(ans)
