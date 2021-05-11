# -*- coding: utf-8 -*-
# @Time    : 2021-05-10 21:04
# @Author  : zxl
# @FileName: 077_2.py

class Solution:

    def recursiveCombine(self,n,idx,k):
        if k == 0:
            return [[]]
        if idx == n+1:
            return []
        ans = []
        for i in range(idx,n+1):
            lst = self.recursiveCombine(n,i+1,k-1)
            for sub_lst in lst:
                sub_lst.insert(0,i)
                ans.append(sub_lst)
        return ans

    def combine(self, n: int, k: int) :

        ans = self.recursiveCombine(n,1,k)
        return ans

obj = Solution()
n = 4
k = 2
ans = obj.combine(n,k)
print(ans)



