# -*- coding: utf-8 -*-
# @Time    : 2021-07-19 17:44
# @Author  : zxl
# @FileName: Baidu01.py


import numpy as np
def solve(num):


    dp = [1 for i in range(num+1)]


    for i in range(2,num+1):

        if int(np.sqrt(i)) ** 2 == i:
            dp[i] = 1
            continue
        min_count = float('inf')

        for j in range(1,i):
            min_count = min(min_count, dp[j]+dp[i-j])
        dp[i] = min_count
    return dp[-1]


num = 11
ans = solve(num)
print(ans)



