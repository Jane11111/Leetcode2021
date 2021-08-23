# -*- coding: utf-8 -*-
# @Time    : 2021-08-08 10:26
# @Author  : zxl
# @FileName: MeiTuan02.py

import sys


def solve(s):
    s = s.replace(' ','')

    i = 0
    ans = ''
    while i<len(s):
        ans+=s[i]
        i+=1
        while i<len(s) and s[i] == s[i-1]:
            i+=1
    return ans

if __name__ == "__main__":


    line = sys.stdin.readline().strip()
    ans = solve(line)
    print(ans)

