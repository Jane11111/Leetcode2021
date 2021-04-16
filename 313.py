# -*- coding: utf-8 -*-
# @Time    : 2021-04-14 22:46
# @Author  : zxl
# @FileName: 313.py


class Solution:
    def nthSuperUglyNumber(self, n , primes ) :

        arr = [1]
        k = len(primes)
        p_lst = [0 for i in range(k)]

        while len(arr)<n:
            v_lst = [arr[p_lst[i]]*primes[i] for i in range(k)]
            min_val = min(v_lst)
            for i in range(k):
                if min_val%primes[i] == 0:
                    p_lst[i]+=1
            arr.append(min_val)

        return arr[n-1]

obj = Solution()
n = 12
primes = [2,7,13,19]
ans = obj.nthSuperUglyNumber(n,primes)
print(ans)
