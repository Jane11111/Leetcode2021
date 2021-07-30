# -*- coding: utf-8 -*-
# @Time    : 2021-07-17 20:56
# @Author  : zxl
# @FileName: 077_5.py


class Solution:

    def recurFind(self,n,idx,k,ans,lst):
        if len(lst) == k:
            ans.append([item for item in lst])

        for i in range(idx,n+1):
            lst.append(i)
            self.recurFind(n,i+1,k,ans,lst)
            lst.pop()
        return

    def combine(self, n: int, k: int) :

        lst = []
        ans = []
        self.recurFind(n,1,k,ans,lst)
        return ans

obj = Solution()
n = 4
k = 2
ans = obj.combine(n,k)
print(ans)
