# -*- coding: utf-8 -*-
# @Time    : 2021-06-18 12:59
# @Author  : zxl
# @FileName: 204.py

class Solution:

    def isPrime(self,lst,n):
        for num in lst:
            if n%num == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:


        if n <=2 :
            return 0


        lst = [2]

        for i in range(3,n):
            if self.isPrime(lst,i):
                lst.append(i)
        return len(lst)




