# -*- coding: utf-8 -*-
# @Time    : 2021-08-21 16:18
# @Author  : zxl
# @FileName: Nest02_2.py




import sys


def solve(names,doc):

    ans = 0
    dic = {}
    for name in names:
        if name[0] not in dic:
            dic[name[0]] = []
        dic[name[0]].append(name)
    for i in range(len(doc)):
        if doc[i] not in dic:
            continue

        for name in dic[doc[i]]:
            if doc[i:i+len(name)] == name:
                ans+=1
    return ans

if __name__ == '__main__':
    line = sys.stdin.readline().strip()

    names = line.split()

    doc = sys.stdin.readline().strip()

    ans = solve(names,doc)
    print(ans)