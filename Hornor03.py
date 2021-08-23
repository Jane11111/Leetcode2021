# -*- coding: utf-8 -*-
# @Time    : 2021-08-10 18:42
# @Author  : zxl
# @FileName: Hornor03.py



import sys
# import heapq

def solve(mat,n):

    visited = []
    for i in range(n):
        visited.append([-1 for j in range(n)])

    if mat[0][0] == 0:
        return -1

    visited[0][0] = 0

    lst = []
    lst.append([0,0,0])
    while len(lst)>0:
        d,x,y = lst.pop(0)

        for newx,newy in [[x-1,y],[x,y-1],[x+1,y],[x,y+1]]:
            if newx>=0 and newx<n and newy>=0 and newy<n and visited[newx][newy] == -1  and mat[newx][newy] == 1:
                newd = d+1
                visited[newx][newy] = newd
                lst.append([newd,newx,newy])
    return visited[n-1][n-1]





if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())

    lst = []
    while n:
        line = sys.stdin.readline().strip()
        arr = list(map(int, line.split()))
        lst.append(arr)

        n-=1
    #
    # n = 5
    # lst = [
    #     [1, 0, 1, 1, 1],
    #     [1, 1, 1, 0, 1],
    #     [1, 1, 0, 0, 1],
    #     [1, 0, 1, 1, 1],
    #     [1, 1, 1, 0, 1]
    # ]

    ans = solve(lst,len(lst))
    print(ans)
