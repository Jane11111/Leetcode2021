# -*- coding: utf-8 -*-
# @Time    : 2021-04-18 21:43
# @Author  : zxl
# @FileName: T001_3.py




import sys

def solve(lst,w):
    i = 0
    j = 1
    while i<len(lst) and j<len(lst):
        if i==j:
            j+=1
        if lst[j]-lst[i] == w:
            return (lst[i],lst[j])
        elif lst[j]-lst[i]>w:
            i+=1
        else:
            j+=1
    return (-1,-1)
def solveAll(lst):
    dic = {}
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            diff = lst[j]-lst[i]
            if diff not in dic:
                dic[diff] = [lst[i],lst[j]]

    return dic


if __name__ == "__main__":
    # 读取第一行的n
    inline = sys.stdin.readline()
    n,m = inline.split()
    n = int(n)
    m = int(m)
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    lst = list(map(int, line.split()))
    lst.sort()
    dic = solveAll(lst)
    for i in range(m):
        w = int(sys.stdin.readline().strip())
        if w not in dic:
            print(-1)
        else:
            print(dic[w][0] ,dic[w][1])
