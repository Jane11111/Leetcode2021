# -*- coding: utf-8 -*-
# @Time    : 2021-08-21 19:24
# @Author  : zxl
# @FileName: JD01.py



import sys

def gcd(a,b):
    if a == 0:
        return 0,1
    if b == 0:
        return 1,0
    old_a, old_b = a,b
    while b:
        tmp = b
        b = a%b
        a = tmp

    return old_a//a,old_b//a

def solve(s):
    n = len(s)

    dic = {i:{} for i in range(n)}
    if s[0] == '0':
        dic[0][1] = {}
        dic[0][1][0] = 1
    if s[0] == '1':
        dic[0][0] = {}
        dic[0][0][1] = 1

    for i in range(1,len(s)):

        zero_count = 0
        one_count = 0

        for j in range(i,-1,-1):
            if s[j] == '0':
                zero_count+=1
            else:
                one_count+=1

            if j==0:
                break
            a,b = gcd(zero_count,one_count)


            if a in dic[j-1] and b in dic[j-1][a]:
                if a not in dic[i]:
                    dic[i][a] = {}
                if b not in dic[i][a]:
                    dic[i][a][b] = 0
                dic[i][a][b] = max(dic[j-1][a][b]+1,dic[i][a][b]) # 可能之前就有过这种比例的

        a,b = gcd(zero_count,one_count)
        if a not in dic[i]:
            dic[i][a] = {}
        if b not in dic[i][a]:
            dic[i][a][b] = 0
        dic[i][a][b] = max(dic[i][a][b],1)
    ans = []
    for i in range(n):
        v = 0
        for a in dic[i]:
            for b in dic[i][a]:
                v = max(v,dic[i][a][b])
        ans.append(v)
    return ans




if __name__ == '__main__':
    N = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    ans = solve(s)
    lst = [str(item) for item in ans]
    print(len(lst))
    s = ' '.join(lst)
    print(s)


