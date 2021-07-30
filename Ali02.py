# -*- coding: utf-8 -*-
# @Time    : 2021-07-20 19:29
# @Author  : zxl
# @FileName: Ali02.py


def merge(lst):
    tmp = []

    i = 0
    while i<len(lst):
        tmp.append(lst[i])
        j = i+1
        while j<len(lst) and lst[j] == lst[j-1]:
            j+=1
        i = j
    return tmp

def setfind(arr,idx):
    if arr[idx] == idx:
        return arr[idx]
    arr[idx] = setfind(arr,arr[idx])
    return arr[idx]
def setmerge(arr,idx1,idx2):

    f1 = setfind(arr,idx1)
    f2 = setfind(arr,idx2)
    arr[f1] = f2

def solve(n,lst):
    lst = merge(lst) # 第一次合并操作

    uniquelist = list(set(lst)) # 所有不同的数字

    uniquelist.sort()

    arr = [i for i in range(len(lst))] # 并查集

    m = len(uniquelist)

    dic = {}
    for i in range(len(lst)):
        if lst[i] not in dic:
            dic[lst[i]] = []
        dic[lst[i]].append(i)

    left = []
    lastleft = len(lst)
    for num in uniquelist:

        for idx in dic[num]: # 遍历所有num对应的位置

            l = lst[idx-1] if idx>0 else float('inf')
            r = lst[idx+1] if idx<len(lst)-1 else float('inf')

            if lst[idx]>l and lst[idx]>r :
                lastleft -=2
                setmerge(arr,idx-1,idx)
                setmerge(arr,idx+1,idx)
            elif lst[idx]>l:
                lastleft -=1
                setmerge(arr,idx-1,idx)
            elif lst[idx]>r:
                lastleft-=1
                setmerge(arr,idx+1,idx)
        left.append(lastleft)
    return m, left


n = 1
lst = [1]
m,left = solve(n,lst)
print(m)
print(left)







