# -*- coding: utf-8 -*-
# @Time    : 2021-03-17 14:21
# @Author  : zxl
# @FileName: 322_2.py


class Solution(object):





    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        arr = [0]
        for i in range(1,amount+1,1):

            min_val = float('inf')
            for coin in coins:
                if i- coin >= 0:
                    min_val = min(min_val,1+arr[i-coin])
            arr.append(min_val)
        if arr[-1] != float('inf'):
            return arr[-1]
        else:
            return -1


obj = Solution()
coins = [346,29,395,188,155,109]
amount = 9401
ans = obj.coinChange(coins,amount)
print(ans)