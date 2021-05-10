# -*- coding: utf-8 -*-
# @Time    : 2021-05-10 14:13
# @Author  : zxl
# @FileName: 795.py

class Solution:
    def numSubarrayBoundedMax(self, A , L: int, R: int) -> int:

        n = len(A)


        arr = [0 for i in range(len(A))]
        for i in range(len(A)):
            if A[i] >=L and A[i]<=R:
                arr[i] = 1
            elif A[i]>R:
                arr[i] = -1
        idx = [[-1,n] for i in range(n)]
        last_idx = -1
        for i in range(n):
            if arr[i]==1:
                idx[i][0] = last_idx
                last_idx = i
            elif arr[i] == -1:
                last_idx = i
        last_idx = n
        for i in range(n-1,-1,-1):
            if arr[i] == -1:
                last_idx = i
            elif arr[i] == 1:
                idx[i][1] = last_idx
        count = 0
        for i in range(n):
            if arr[i] == 1:
                li = idx[i][0]
                ri = idx[i][1]
                num1 = i-li
                num2 = ri-i
                count += num1*num2
        return count





obj = Solution()
A = [2, 1, 4, 3]
L = 2
R = 3
ans = obj.numSubarrayBoundedMax(A,L,R)
print(ans)

