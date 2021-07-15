# -*- coding: utf-8 -*-
# @Time    : 2021-07-14 15:08
# @Author  : zxl
# @FileName: 060_2.py


class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        if n == 1:
            return '1'

        mul = [1]
        for i in range(2,n+1):
            mul.insert(0,mul[0]*i)
        lst = [i for i in range(1,n+1)]
        ans = ''

        for i in range(n):

            if i+1 == n:
                ans += str(lst[0])
                break
            a = k//mul[i+1]
            b = k%mul[i+1]
            if b>0:
                a+=1
            k = b if b>0 else mul[i+1]
            num = lst.pop(a-1)
            ans+=str(num)
        return ans

obj = Solution()
n = 3
k = 1
ans = obj.getPermutation(n,k)
print(ans)