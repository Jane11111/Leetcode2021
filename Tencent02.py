# -*- coding: utf-8 -*-
# @Time    : 2021-08-22 21:10
# @Author  : zxl
# @FileName: Tencent02.py



import sys


def solve(step,pi,mat):

    if step == 0:
        return pi

    new_pi = [0 ,0,0]

    for i in range(3):
        val = 0
        for j in range(3):
            val += mat[i][j] * pi[j]
        new_pi[i] = val
    return solve(step-1,new_pi,mat)







if __name__ == '__main__':

    T = int(sys.stdin.readline().strip())

    while T:

        step = int(sys.stdin.readline().strip())

        line = sys.stdin.readline().strip()
        pi = list(map(float, line.split()))

        mat = []
        for i in range(3):
            line = sys.stdin.readline().strip()
            arr = list(map(float, line.split()))
            mat.append(arr)
        ans = solve(step,pi,mat)
        if ans[2]>0.5:
            print(1)
        else:
            print(0)

        T-=1
