# -*- coding: utf-8 -*-
# @Time    : 2021-08-08 10:53
# @Author  : zxl
# @FileName: MeiTuan04.py



import sys

def find(fa,x):
    if fa[x] == x:
        return fa[x]
    fa[x] = find(fa,fa[x])
    return fa[x]
def merge(arr,x,y):
    f1 = find(arr,x)
    f2 = find(arr,y)
    arr[f1] = f2



def solve(arr):

    fa = [i for i in range(100000+1)]
    dic = {}


    m = len(arr)//2

    for i in range(m):


        if arr[i] != arr[m+i]:
            dic[arr[i]] = True
            dic[arr[m+i]] = True
            merge(fa,arr[i],arr[m+i])

    dic2 = {}
    for i in range(1,100000+1):
        if i not in dic:
            continue
        f = find(fa,i)
        dic2[f] = True

    return len(dic) - len(dic2)



if __name__ == "__main__":


    N = sys.stdin.readline().strip()
    line = sys.stdin.readline().strip()
    arr = list(map(int, line.split()))

    ans = solve(arr)
    print(ans)
# arr = [4 ,2, 1, 5, 2, 10, 2, 1, 5, 8]
# ans = solve(arr)
# print(ans)