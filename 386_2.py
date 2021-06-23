# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 21:57
# @Author  : zxl
# @FileName: 386_2.py


class Solution:

    def dfs(self,n,t,lst):
        if t<=n:
            lst.append(t)
        else:
            return
        for i in range(10):
            self.dfs(n,t*10+i,lst)



    def lexicalOrder(self, n: int):

        ans = []

        for i in range(1,10):
            self.dfs(n,i,ans)
        return ans


obj =Solution()
n = 201
ans = obj.lexicalOrder(n)
print(len(ans))
print(ans)
