# -*- coding: utf-8 -*-
# @Time    : 2021-08-16 17:46
# @Author  : zxl
# @FileName: 004_9.py


def findK(arr1, arr2, k):
    s1 = 0
    e1 = len(arr1) - 1
    s2 = 0
    e2 = len(arr2) - 1
    while s1 <= e1 and s2 <= e2:

        m1 = (s1 + e1) // 2
        m2 = (s2 + e2) // 2

        if (m1 - s1 + m2 - s2 + 2) > k:
            if arr1[m1] >= arr2[m2]:
                e1 = m1 - 1
            else:
                e2 = m2 - 1
        else:
            if arr1[m1] <= arr2[m2]:
                k -= (m1 - s1 + 1)
                s1 = m1 + 1
            else:
                k -= (m2 - s2 + 1)
                s2 = m2 + 1

    if s1 > e1:
        return arr2[s2 + k - 1]
    # print(s1)
    # print(k)
    return arr1[s1 + k - 1]


def solve(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    if (n1 + n2) % 2 == 1:
        k = 1 + (n1 + n2) // 2
        return findK(arr1, arr2, k)
    else:
        k1 = (n1 + n2) // 2
        k2 = k1 + 1
        num1 = findK(arr1, arr2, k1)
        num2 = findK(arr1, arr2, k2)
        print(num1)
        print(num2)
        return (num1 + num2) / 2

arr1 = [1,3]
arr2 = [5,7]
ans = solve(arr1,arr2)
print(ans)