# -*- coding: utf-8 -*-
# @Time    : 2021-04-03 10:57
# @Author  : zxl
# @FileName: 739.py

class Solution:
    def dailyTemperatures(self, T):

        n = len(T)

        lst = []
        arr = [0 for i in range(n)]

        for i in range(n):
            if len(lst) == 0 or T[i]<=T[lst[-1]]:
                lst.append(i)
            else:

                while len(lst) > 0 and T[i]>T[lst[-1]]:
                    arr[lst[-1]] = i-lst[-1]
                    lst.pop()
                lst.append(i)
        return arr

obj = Solution()
T= [73, 74, 75, 71, 69, 72, 76, 73]
ans = obj.dailyTemperatures(T)
print(ans)