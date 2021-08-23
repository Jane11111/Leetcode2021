# -*- coding: utf-8 -*-
# @Time    : 2021-08-10 18:27
# @Author  : zxl
# @FileName: Hornor01.py




import sys

def solve(lst):

    query = lst[-1].split('=')[1]
    lst = lst[:-1]

    dict = {}
    while len(lst)>0:

        i = 0
        while i<len(lst):
            s = lst[i]
            if '$' not in s:
                arr = s.split('=')
                dict[arr[0]] = arr[1]
                lst.pop(i)
            else:
                for k in dict:
                    lst[i] = lst[i].replace('${'+k+'}',dict[k])


                i+=1
    for k in dict:
        query = query.replace('${'+k+'}',dict[k])
    return query



if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())

    lst = []
    while n:
        line = sys.stdin.readline().strip()

        lst.append(line)


        n-=1
    ans = solve(lst)
    print(ans)