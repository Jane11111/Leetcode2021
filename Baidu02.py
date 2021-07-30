# -*- coding: utf-8 -*-
# @Time    : 2021-07-19 17:50
# @Author  : zxl
# @FileName: Baidu02.py







def solve(s,target):
    if len(s) == 0:
        return 0

    if len(s) == 1:
        return int(s) == target

    num = int(s[0])
    n1 = solve(s[1:],target-num)
    n2 = solve(s[1:],num-target)
    return n1+n2

s = '111111'
target = 4
ans = solve(s,target)
print(ans)


