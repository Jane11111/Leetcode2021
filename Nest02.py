# -*- coding: utf-8 -*-
# @Time    : 2021-08-21 15:04
# @Author  : zxl
# @FileName: Nest02.py


import sys


def solve(names,doc):

    dic = {}

    for name in names:

        p = dic
        for c in name :
            if c not in p:
                p[c] = {}
                p = p[c]
        if 'isend' not in p:
            p['isend'] = 0
        p['isend'] +=1

    i = 0
    ans = 0
    while i<len(doc):

        if doc[i] not in dic:
            i += 1
            continue
        p = dic
        j = i
        while j<len(doc) and doc[j] in p:
            p = p[doc[j]]
            if 'isend' in p:
                ans += p['isend']
            j += 1
        i += 1
    return ans

if __name__ == '__main__':
    line = sys.stdin.readline().strip()

    names = line.split()

    doc = sys.stdin.readline().strip()

    ans = solve(names,doc)
    print(ans)