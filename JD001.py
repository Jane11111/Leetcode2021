# -*- coding: utf-8 -*-
# @Time    : 2021-04-24 19:36
# @Author  : zxl
# @FileName: JD001.py

import sys


def solve(nums,k):

    n = len(nums)



    pos = (k//2)+1
    v = sum(nums[:k])
    max_val = v

    for i in range(k,n):

        v = v+nums[i]-nums[i-k]
        if v>max_val:
            max_val = v
            pos = (i+i-k+1)//2+1
    return pos





if __name__ == "__main__":
    # 读取第一行的n
    inline = sys.stdin.readline().strip()
    n,k = inline.split()
    n = int(n)
    k = int(k)

    line = sys.stdin.readline().strip()
    values = list(map(float, line.split()))

    if n == 1:
        print(1)
    else:
        num = solve(values,k)
        print(num)




