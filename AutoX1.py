# -*- coding: utf-8 -*-
# @Time    : 2021-07-05 19:21
# @Author  : zxl
# @FileName: AutoX1.py



import sys


def solve(rectangles, nums,K):
    ans = 0

    for i in range(len(rectangles)):

        x1,y1,x2,y2 = rectangles[i]
        m = nums[i]
        if m<K:
            continue

        ans += abs((x2-x1)*(y2-y1))
    return ans



if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))

    N , K = values
    rectangles = []
    nums = []
    for i in range(N):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))

        rectangles.append(values[:4])
        nums.append(values[-1])

    ans = solve(rectangles,nums,K)
    print(ans)
