# -*- coding: utf-8 -*-
# @Time    : 2021-08-21 16:30
# @Author  : zxl
# @FileName: 135_2.py


class Solution:
    def candy(self, arr) -> int:
        n = len(arr)
        l2r = [1 for i in range(n)]
        r2l = [1 for i in range(n)]

        # min_idx = 0
        # for i in range(n):
        #     if arr[i] < arr[min_idx]:
        #         min_idx = i

        for num in range(1,n):
            i = num % n
            ni = i - 1
            if arr[i] > arr[ni]:
                l2r[i] = l2r[ni] + 1
        for num in range(n-2,-1,-1):
            # if arr[i] == arr[i+1]:
            #     r2l[i] = r2l[i+1]
            i = num
            ni = i + 1
            if arr[i] > arr[ni]:
                r2l[i] = r2l[ni] + 1
        ans = 0
        for i in range(n):
            ans += max(l2r[i], r2l[i])
        return ans
obj = Solution()
arr = [1,0,2]
ans = obj.candy(arr)
print(ans)