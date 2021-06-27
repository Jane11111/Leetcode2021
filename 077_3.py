# -*- coding: utf-8 -*-
# @Time    : 2021-06-26 16:47
# @Author  : zxl
# @FileName: 077_3.py


class Solution:


    def recFind(self,n,start,k,lst):

        if len(lst) == k:
            return [[item for item in lst]]
        if n-start+1 < k-len(lst):
            return []
        ans = []
        for i in range(start,n+1):
            lst.append(i)
            cur_ans = self.recFind(n,i+1,k,lst)
            ans.extend(cur_ans)
            lst.pop()
        return ans



    def combine(self, n: int, k: int) :

        ans = self.recFind(n,1,k,[])
        return ans

obj = Solution()
n = 4
k = 2
ans = obj.combine(n,k)
print(ans)