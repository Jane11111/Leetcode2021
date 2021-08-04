# -*- coding: utf-8 -*-
# @Time    : 2021-08-01 15:30
# @Author  : zxl
# @FileName: aiqiyi02.py

def findMaxArea(arr):


    area = 0

    lst = []
    for i in range(len(arr)):
        while len(lst) and arr[i]< arr[lst[-1]]:
            idx = lst.pop()
            l = -1 if len(lst) == 0 else lst[-1]
            cur_height = arr[idx]
            cur_width = i-l-1
            cur_area = min(cur_height,cur_width)**2
            area = max(area,cur_area)
        lst.append(i)
    n = len(arr)

    while len(lst):
        idx = lst.pop()
        l = -1 if len(lst) == 0 else lst[-1]
        cur_height = arr[idx]
        cur_width = n - l - 1
        cur_area = min(cur_height, cur_width) ** 2
        area = max(area, cur_area)
    return area

def solve(matrix):
    m = len(matrix)
    n = len(matrix[0])

    dp = []
    for i in range(m):
        dp.append([0 for j in range(n)])

    for j in range(n):
        dp[0][j] = matrix[0][j]

    for i in range(1,m):
        for j in range(n):
            if matrix[i][j] == 1:
                dp[i][j] = 1+dp[i-1][j]
    ans = 0

    for i in range(m):
        arr = dp[i]
        val = findMaxArea(arr)
        ans = max(ans,val)
    return ans


raw_input = input("")

m = raw_input.split(';')

matrix = []

for line in m:

    elements = line.split(',')

    matrix.append([int(item) for item in elements])

ans = solve(matrix)
print(ans)