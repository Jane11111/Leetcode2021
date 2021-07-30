# -*- coding: utf-8 -*-
# @Time    : 2021-07-19 17:59
# @Author  : zxl
# @FileName: Baidu03.py



def solve(s,target):

    if len(s) == 0:
        return 0

    if len(s) == 1:
        return int(s) == target


    lst = [int(s[0])]

    for i in range(1,len(s)):

        num = int(s[i])

        tmp = []
        for j in range(len(lst)):

            new_num1 = lst[j]-num
            new_num2 = lst[j]+num
            tmp.append(new_num1)
            tmp.append(new_num2)
        lst = tmp
    count = 0
    for num in lst:
        if num == target:
            count += 1
    return count

s = '111111'
target = 2
ans = solve(s,target)
print(ans)

