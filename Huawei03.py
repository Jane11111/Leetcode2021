# -*- coding: utf-8 -*-
# @Time    : 2021-08-18 19:24
# @Author  : zxl
# @FileName: Huawei03.py



import sys

def recSolve(M,N,mat,x,y,tx,ty, visited):

    if abs(tx-x)+abs(ty-y) == 1:

        if x-tx == 1:
            d0 = 1
        else:
            d0 = float('inf')
        if ty-y == 1:
            d1 = 1
        else:
            d1 = float('inf')
        if tx-x == 1:
            d2 = 1
        else:
            d2 = float('inf')
        if y-ty == 1:
            d3 = 1
        else:
            d3 = float('inf')

        return [d0,d1,d2,d3]
    # ans = 0
    # if x == tx and y == ty:
    #     return [0,0,0,0]
    arr = [float('inf'),float('inf'),float('inf'),float('inf')]
    for idx in range(4):
        newx,newy =[[x-1,y],[x,y+1],[x+1,y],[x,y-1]][idx]
        if newx<0 or newy<0 or newx>=M or newy>=N:
            continue
        v = float('inf')
        if not visited[newx][newy] and mat[newx][newy] == 0:
            visited[newx][newy] = True
            d0,d1,d2,d3 = recSolve(M,N,mat,newx,newy,tx,ty,visited)
            if d0!=float('inf'):
                if idx == 0:
                    v = min(v,d0)
                else:
                    v = min(v,d0+1)
            if d1!=float('inf'):
                if idx == 1:
                    v = min(v,d1)
                else:
                    v = min(v,d1+1)
            if d2!=float('inf'):
                if idx == 2:
                    v = min(v,d2)
                else:
                    v = min(v,d2+1)
            if d3!=float('inf'):
                if idx == 3:
                    v = min(v,d3)
                else:
                    v = min(v,d3+1)
            visited[newx][newy] = False
        # if v != float('inf'):
        arr[idx] = v
    return arr


def solve(M,N,mat,x1,y1,x2,y2):
    visited = []

    for i in range(M):
        visited.append([False for j in range(N)])

    visited[x1][y1] = True

    d0,d1,d2,d3 = recSolve(M,N,mat,x1,y1,x2,y2,visited)

    return min([d0,d1,d2,d3])

if __name__ == "__main__":
    line = sys.stdin.readline().strip()

    M,N = list(map(int, line.split()))

    mat = []

    for i in range(M):
        line = sys.stdin.readline().strip()

        arr = list(map(int, line.split()))
        mat.append(arr)

    line = sys.stdin.readline().strip()

    x1,y1,x2,y2 = list(map(int, line.split()))
    ans = solve(M,N,mat,x1,y1,x2,y2)
    print(ans)

