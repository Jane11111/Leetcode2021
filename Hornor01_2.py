# -*- coding: utf-8 -*-
# @Time    : 2021-08-10 19:08
# @Author  : zxl
# @FileName: Hornor01_2.py



import sys

def find(k,dic):

    v = dic[k]
    if '$' not in v:
        return v
    i = 0
    tmp =''
    while i<len(v):
        if v[i]!= '$':
            tmp+=v[i]
            i+=1
            continue

        j = i+2
        while j<len(v) and v[j] !='}':
            j+=1

        newk = v[i+2:j]

        newv = find(newk,dic)
        tmp+=newv


        i = j+1
    dic[k] = tmp
    return tmp




def solve(lst):
    dic = {}
    for i in range(len(lst)):
        arr = lst[i].split('=')
        dic[arr[0]] = arr[1]
    k = lst[-1].split('=')[0]
    ans = find(k,dic)

    return ans

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())

    lst = []
    while n:
        line = sys.stdin.readline().strip()

        lst.append(line)


        n-=1

    # lst = [
    # 'xxx=lyf/${ttt}/test',
    # 'ttt=www',
    # 'yyy=seeyou',
    # 'aa=/aaa/${xxx}/bbb/${yyy}/ccc'
    #
    # ]
    ans = solve(lst)
    print(ans)