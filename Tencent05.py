# -*- coding: utf-8 -*-
# @Time    : 2021-08-22 20:41
# @Author  : zxl
# @FileName: Tencent05.py



import sys

def explore_dfs(mat,i,j,n,visited ):

    if i<0 or j<0 or i == n or j == n:
        return True

    visited[i][j] = True

    can_out = False
    for x,y in [[i-1,j],[i,j-1],[i+1,j],[i,j+1]]:

        if x<0 or y<0 or x == n or y== n or (not visited[x][y] and mat[x][y] == '0'):

            f = explore_dfs(mat,x,y,n,visited )
            if f:
                can_out = True
    if can_out:
        mat[i][j] = '3'
    return can_out

def mark_dfs(mat,i,j,n,visited):

    if i<0 or j<0 or i == n or j == n:
        return

    visited[i][j] = True
    mat[i][j] = '3'

    for x,y in [[i-1,j],[i,j-1],[i+1,j],[i,j+1]]:
        if x<0 or y<0 or x == n or y == n or (not visited[x][y] and (mat[x][y] == '0' or mat[x][y] == '3')):
            mark_dfs(mat,x,y,n,visited)


def solve(mat,n):

    visited = []

    for i in range(n):
        visited.append([False for j in range(n)])

    for i in range(n):
        for j in range(n):
            if mat[i][j] == '0' and not visited[i][j]:
                explore_dfs(mat,i,j,n,visited)

    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    for i in range(n):
        for j in range(n):
            if mat[i][j] == '3' :
                mark_dfs(mat,i,j,n,visited)

    for i in range(n):

        for j in range(n):
            if mat[i][j] == '3':
                mat[i][j] = '0'
            elif mat[i][j] == '0':
                mat[i][j] = '2'






if __name__ == '__main__':

    n = int(sys.stdin.readline().strip())
    mat = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        arr = list(map(str, line.split()))
        mat.append(arr)
    solve(mat,n)
    for arr in mat:
        print(' '.join(arr))


