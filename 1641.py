# -*- coding: utf-8 -*-
# @Time    : 2021-08-02 10:16
# @Author  : zxl
# @FileName: 1641.py


class Solution:

    def recFind(self,n,voc,idx,s,ans):

        if len(s) == n:
            ans.append(s)
            return
        if idx>=len(voc):
            return

        for i in range(idx,len(voc)):
            news = s+voc[i]
            self.recFind(n,voc,i,news,ans)

    def countVowelStrings(self, n: int) -> int:


        voc = ['a','e','i','o','u']
        ans = []
        self.recFind(n,voc,0,'',ans)
        return len(ans)


obj = Solution()

n = 5

ans = obj.countVowelStrings(n)
print(ans)

