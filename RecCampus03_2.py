# -*- coding: utf-8 -*-
# @Time    : 2021-08-21 11:03
# @Author  : zxl
# @FileName: RecCampus03_2.py


import sys



def calInterval(s1,s2):

    h1 = int(s1[:2])
    m1 = int(s1[3:])

    h2 = int(s2[:2])
    m2 = int(s2[3:])

    ans = 60*h2+m2-60*h1-m1
    return ans


def calAllInterval(lst):
    time_lst = [0 for i in range(len(lst))]

    for i in range(len(lst)):
        time_lst[i] = calInterval(lst[i][0],lst[i][1])
    return time_lst

def solve(lst):


    lst.sort()
    if len(lst)<3:
        return 0
    time_lst = calAllInterval(lst)
    ans = float('-inf')

    for i in range(1,len(lst)-1):

        t1 = time_lst[i]
        t2 = float('-inf')
        for j in range(i):
            if lst[j][1]<=lst[i][0]:
                cur_t = time_lst[j]
                t2 = max(t2,cur_t)
        t3 = float('-inf')
        for j in range(i+1,len(lst)):
            if lst[j][0] >= lst[i][1]:
                cur_t = time_lst[j]
                t3 = max(t3, cur_t)
        if t2 == float('-inf') or t3 == float('-inf'):
            continue
        ans = max(ans,t1+t2+t3)
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