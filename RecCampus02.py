# -*- coding: utf-8 -*-
# @Time    : 2021-08-21 10:27
# @Author  : zxl
# @FileName: RecCampus02.py


import sys

def mat2s(mat):

    s = ''
    for i in range(len(mat)):
        s+=''.join(mat[i])
    return s


def dfs(mat,x,y,m,n,visited,cur_count,total_count,dic,cur_s):
    if cur_count == total_count and x == m-1:
        return 1
    if cur_count == total_count:
        return 0
    if x in dic and y in dic[x] and cur_s in dic[x][y]:
        return dic[x][y][cur_s]

    ans = 0

    for i,j in [[x-1,y],[x,y-1],[x+1,y],[x,y+1]]:

        if i<0 or i>=m or j<0 or j>=n or mat[i][j] == '#'  :
            continue

        mat[i][j] = '#'
        pos = i*m+j
        new_s = cur_s[:pos]+'#'+cur_s[pos+1:]
        ans+=dfs(mat,i,j,m,n,visited,cur_count+1,total_count,dic,new_s)
        mat[i][j] = '.'


    if x not in dic:
        dic[x] = {}
    if y not in dic[x]:
        dic[x][y] = {}
    dic[x][y][cur_s] = ans

    return ans

def solve(mat):


    m = len(mat)
    n = len(mat[0])

    visited = []
    total_count = 0
    for i in range(m):
        visited.append([False for j in range(n)])
        for j in range(n):
            if mat[i][j] == '.':
                total_count+=1
    cur_count = 0
    if mat[0][0] == '.':
        cur_count += 1
    visited[0][0] = True
    mat[0][0] = '#'
    cur_s = mat2s(mat)
    ans = dfs(mat,0,0,m,n,visited,cur_count,total_count,{},cur_s)
    return ans




if __name__ == "__main__":

    N = int(sys.stdin.readline())

    mat = []
    while N:
        line = sys.stdin.readline().strip()
        arr = [c for c in line]
        mat.append(arr)

        N-=1
    ans = solve(mat)
    print(ans)



