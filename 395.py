# -*- coding: utf-8 -*-
# @Time    : 2021-03-20 10:35
# @Author  : zxl
# @FileName: 395.py


class Solution:

    def dfs(self,s,p,q,k):
        if q-p+1<k:
            return 0


        dic = {}
        for i in range(p,q+1):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] +=1


        ans = float('-inf')
        last_p = p
        for i in range(p,q+1):
            if dic[s[i]]<k :
                l = self.dfs(s,last_p,i-1,k)
                ans = max(ans,l)
                last_p = i+1
            elif i == q:
                if last_p == p:
                    ans = max(ans,i-p+1)
                else:
                    l = self.dfs(s, last_p, i , k)
                    ans = max(ans, l)
                    last_p = i + 1

        return ans



    def longestSubstring(self, s: str, k: int) -> int:


        ans = self.dfs(s,0,len(s)-1,k)
        return ans


s = 'a'
k = 3
obj = Solution()
ans = obj.longestSubstring(s,k)
print(ans)
