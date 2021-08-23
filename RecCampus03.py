# -*- coding: utf-8 -*-
# @Time    : 2021-08-21 10:39
# @Author  : zxl
# @FileName: RecCampus.py



import sys

def calInterval(s1,s2):

    h1 = int(s1[:2])
    m1 = int(s1[3:])

    h2 = int(s2[:2])
    m2 = int(s2[3:])

    ans = 60*h2+m2-60*h1-m1
    return ans

def findTwo(lst):

    if len(lst)<2:
        return -1

    i = 0
    ans = float('-inf')
    while i<len(lst):
        t1 = calInterval(lst[i][0],lst[i][1])
        for j in range(i+1,len(lst)):
            if lst[j][0]<lst[i][1]:
                continue
            t2 = calInterval(lst[j][0],lst[j][1])
            ans = max(ans,t1+t2)
        i+=1
    if ans == float('-inf'):
        return -1
    return ans


def solve(lst):
    if len(lst)<3:
        return 0
    lst.sort()

    i = 0
    ans = float('-inf')
    while i<len(lst):
        t1 = calInterval(lst[i][0],lst[i][1])
        j = 0
        while j<len(lst) and lst[j][1]<lst[i][0]:
            j+=1
        t23 = findTwo(lst[j:])
        if t23 == -1:
            continue
        ans = max(ans,t1+t23)
        i+=1
    if ans == float('-inf'):
        return 0
    return ans



if __name__ == "__main__":

    N = int(sys.stdin.readline())

    lst = []
    while N:
        line = sys.stdin.readline().strip()
        lst.append(line.split('-'))
        N-=1
    ans = solve(lst)
    print(ans)