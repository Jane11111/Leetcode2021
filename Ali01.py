# -*- coding: utf-8 -*-
# @Time    : 2021-07-20 19:00
# @Author  : zxl
# @FileName: Ali01.py



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


def down(lst):

    min_len = float('inf')
    for num in lst:
        if num!=0:
            min_len = min(min_len,num)


    for i in range(len(lst)):
        if lst[i]!=0:
            lst[i] -= min_len
    return lst

def solve(n,lst):


    lst = merge(lst)

    m = 0
    left = []
    if len(lst) == 1:
        m = 1
        left = [0]

    while len(lst)!=1:
        m+=1
        lst = down(lst)
        lst = merge(lst)
        left.append(len(lst))
    # m+=1
    # left.append(1)
    return m,left

n = 1
lst = [1 ]
m,left = solve(n,lst)
print(m)
print(left)
