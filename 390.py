# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 22:13
# @Author  : zxl
# @FileName: 390.py



class Solution:

    def recPop(self,lst,d):
        if len(lst) == 1:
            return
        if d == 0:
            i = 0
            while True:
                lst.pop(i)
                i+=1
                if i>=len(lst):
                    break
        else:

            i = len(lst)-1
            while True:
                lst.pop(i)
                i-=2
                if i<0:
                    break


    def lastRemaining(self, n: int) -> int:

        d = 0
        lst = [i for i in range(1,n+1)]
        while len(lst)>1:
            self.recPop(lst,d)
            d^=1
        return lst[0]

obj = Solution()
n = 9
ans = obj.lastRemaining(n)
print(ans)
