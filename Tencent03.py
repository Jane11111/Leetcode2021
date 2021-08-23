# -*- coding: utf-8 -*-
# @Time    : 2021-08-22 20:23
# @Author  : zxl
# @FileName: Tencent02.py


import sys

def solve(lst):
    lst.sort()

    ans = 0
    last_idx = -1

    i = 0
    while i<len(lst):


        while lst[i]-lst[last_idx+1]>10:
            last_idx+=1
        ans = max(ans,i-last_idx)
        i+=1
    return ans


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    lst = list(map(int, line.split()))


    ans = solve(lst)
    print(ans)