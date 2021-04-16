# -*- coding: utf-8 -*-
# @Time    : 2021-04-14 21:25
# @Author  : zxl
# @FileName: 1201.py


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:


        i= 1
        j = 1
        k = 1
        arr = []
        while len(arr) < n:
            va = a*i
            vb = b*j
            vc = c*k
            min_val = min([va,vb,vc])

            if min_val%a == 0:
                i+=1
            if min_val %b == 0:
                j+=1
            if min_val %c == 0:
                k+=1
            arr.append(min_val)
        return arr[n-1]



obj = Solution()
n = 3
a = 2
b = 3
c = 5
ans = obj.nthUglyNumber(n,a,b,c)
print(ans)