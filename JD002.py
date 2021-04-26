# -*- coding: utf-8 -*-
# @Time    : 2021-04-24 19:47
# @Author  : zxl
# @FileName: JD002.py



import sys


def solve(n,used,last_pos,last_val):
    if last_pos == n-1:
        return 1

    # if last_pos-8 in used and not used[last_pos-8]:
    #     return 0


    count = 0
    lst = [last_val-1,last_val-2,last_val+1,last_val+2]
    for v in lst:
        if not used[v]:
            used[v] = True
            count+=solve(n,used,last_pos+1,v)
            used[v] = False
            v+=1
    return count %998244353



if __name__ == "__main__":
    # 读取第一行的n
    n = sys.stdin.readline().strip()
    n = int(n)

    used = {i:False for i in range(1,n)}
    used[0] = True
    used[-1] = True
    used[-2] = True
    used[-3] = True
    used[-4] = True
    used[-5] = True
    used[n] = True
    used[n+1] = True
    used[n+2] = True
    num = solve(n,used,0,0)
    print(num)

