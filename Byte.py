# -*- coding: utf-8 -*-
# @Time    : 2021-05-09 20:50
# @Author  : zxl
# @FileName: Byte.py


import sys



def solve(N, lst):
    dic = {}
    for i in range(1, N + 1):
        dic[i] = {'parent': -1, 'child': set()}
    for c, p in lst:
        c = int(c)
        p = int(p)
        # print(dic[p])
        # if dic[p]['parent'] == -1:
        #    print('aaa')

        if dic[p]['parent'] != -1:
            parent_id = dic[p]['parent']
            dic[c]['parent'] = parent_id
            dic[parent_id]['child'].add(c)
            for ch in dic[c]['child']:
                dic[ch]['parent'] = parent_id
        else:
            dic[c]['parent'] = p
            dic[p]['child'].add(c)
            for ch in dic[c]['child']:  # change parent
                dic[ch]['parent'] = p
    max_count = 1
    for k in dic:
        max_count = max(max_count, 1 + len(dic[k]['child']))
    return max_count


if __name__ == "__main__":

    # line = sys.stdin.readline().strip()
    # N, K = line.split()
    N = 5
    K = 5
    lst = [[3,2],[4,3],[3,1],[5,3],[5,5]]


    ans = solve(N, lst)
    print(ans)