# -*- coding: utf-8 -*-
# @Time    : 2021-05-07 13:40
# @Author  : zxl
# @FileName: Offer060.py


class Solution:

    def allCombination(self,n,target,min_val,dic):
        if target == 0 and n == 0:
            return 1
        if target<0  or(n==0 and target!=0) or (n!=0 and target==0):
            return 0

        if n in dic and target in dic[n]:
            return dic[n][target]

        count = 0
        for i in range(1,7):
            count += self.allCombination(n-1,target-i,i,dic)
        if n not in dic:
            dic[n] = {}
        dic[n][target] = count
        # dic[n][6*n-target] = count
        return count

    def dicesProbability(self, n )  :

        deno = 6**n

        ans = []
        for i in range(n,6*n+1):
            c = self.allCombination(n,i,0,{})
            ans.append(c/deno)

        return ans

obj = Solution()
n = 2
ans = obj.dicesProbability(n)
print(ans)




