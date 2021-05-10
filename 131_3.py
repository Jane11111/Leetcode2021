# -*- coding: utf-8 -*-
# @Time    : 2021-05-10 13:17
# @Author  : zxl
# @FileName: 131_3.py

class Solution:

    def recursivePartition(self,s,i,j,dic,dp):
        if i in dic and j in dic[i]:
            return dic[i][j]
        if i not in dic:
            dic[i] = {}

        if i == j:
            dic[i][j] = [[s[i]]]
            return dic[i][j]
        ans = []
        if dp[i][j] :
            ans.append([s[i:j+1]])
        # if i == 0 and j == 3:
        #     print('i am here')
        for k in range(i,j):
            # l = self.recursivePartition(s,i,k,dic,dp)
            if dp[i][k]:
                l = [[s[i:k+1]]]
            else:
                continue
            r = self.recursivePartition(s,k+1,j,dic,dp)
            # if k == i:
            for lst1 in l:
                if k>i and len(lst1[-1]) == 1:
                    continue
                for lst2 in r:
                    tmp = [item for item in lst1]
                    tmp.extend(lst2)
                    ans.append(tmp)
        dic[i][j] = ans
        return ans

    def partition(self, s: str) :

        n = len(s)
        dp = []
        for i in range(n):
            dp.append([True for j in range(n)])

        for l in range(2,n+1):
            for i in range(n):
                j = i+l-1
                if j>=n:
                    break
                if s[i]!=s[j]:
                    dp[i][j] = False
                else:
                    dp[i][j] = True if j-i==1 else dp[i+1][j-1]
        dic = {}
        ans = self.recursivePartition(s,0,n-1,dic,dp)
        return ans

obj = Solution()
s = "abbab"
ans = obj.partition(s)
print(ans)





