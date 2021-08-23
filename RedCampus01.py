# -*- coding: utf-8 -*-
# @Time    : 2021-08-21 10:09
# @Author  : zxl
# @FileName: RedCampus01.py

import sys

def recSolve(lst,idx,n1_count,n2_count,dic):

    if idx == len(lst) and n1_count == 0 and n2_count == 0:
        return 0

    if idx in dic and n1_count in dic[idx] and n2_count in dic[idx][n1_count]:
        return dic[idx][n1_count][n2_count]
    if idx not in dic:
        dic[idx] = {}
    if n1_count not in dic[idx]:
        dic[idx][n1_count] = {}
    # if n2_count not in dic[idx][n1_count]:

    ans = 0
    if n1_count == 0:
        for i in range(idx,len(lst)):
            ans+=lst[i][1]
    elif n2_count == 0:
        for i in range(idx,len(lst)):
            ans+=lst[i][0]
    else:
        ans1 = lst[idx][0]+recSolve(lst,idx+1,n1_count-1,n2_count,dic)
        ans2 = lst[idx][1] + recSolve(lst,idx+1,n1_count,n2_count-1,dic)
        ans = min(ans1,ans2)

    dic[idx][n1_count][n2_count]=ans
    return ans


def solve(data):

    n1 = 0
    n2 = 0

    lst = []

    for arr in data:
        if arr[0] == 1:
            n1+=1
        elif arr[0] == 2:
            n2+=1
        else:
            lst.append(arr[1:])

    if len(lst)<abs(n1-n2) or (len(lst)-abs(n1-n2))%2 == 1:
        return -1
    n1_count = (len(lst)-abs(n1-n2))//2
    n2_count = n1_count
    if n1>n2:
        n2_count+=(n1-n2)
    else:
        n1_count+=(n2-n1)
    return recSolve(lst,0,n1_count,n2_count,{})



if __name__ == "__main__":


    N = int(sys.stdin.readline())

    lst = []
    while N:
        line = sys.stdin.readline()
        arr = list(map(int, line.split()))
        lst.append(arr)
        N-=1
    ans = solve(lst)
    print(ans)


    # lst = list(map(int, line.split()))
