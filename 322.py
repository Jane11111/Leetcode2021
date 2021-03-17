# -*- coding: utf-8 -*-
# @Time    : 2021-03-17 13:26
# @Author  : zxl
# @FileName: 322.py


# TODO 超时

class Solution(object):
    def recursiveFind(self,coins,amount,start_index):

        if amount<0:
            return -1
        if amount == 0:
            return 0
        if start_index >= len(coins):
            return -1

        if start_index == len(coins)-1:
            if amount%coins[-1] != 0:
                return -1
        if amount < coins[-1] :
            return -1


        ans = 10001

        for i in range(start_index,len(coins)):

            for j in range(int(amount//coins[i])+1,-1,-1):
                if j >= ans:
                    break
                if j*coins[i] > amount:
                    continue
                k = self.recursiveFind(coins,amount-j*coins[i],i+1)
                if k == -1:
                    continue
                ans = min(ans,j+k)
                if k == 0:
                    return ans
        if ans == 10001:
            ans = -1
        return ans





    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        coins.sort(reverse=True)
        ans = self.recursiveFind(coins,amount,0)
        return ans


obj = Solution()
coins = [346,29,395,188,155,109]
amount = 9401
ans = obj.coinChange(coins,amount)
print(ans)

