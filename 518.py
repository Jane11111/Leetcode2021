# -*- coding: utf-8 -*-
# @Time    : 2021-05-18 21:30
# @Author  : zxl
# @FileName: 518.py



class Solution:


    def recChange(self,amount,coins,idx,dic):
        if amount == 0 :
            return 1

        if amount < 0 or idx>=len(coins):
            return 0
        if idx in dic and amount in dic[idx]:
            return dic[idx][amount]
        ans = 0
        for j in range(amount//coins[idx]+1):
            ans+=self.recChange(amount-j*coins[idx],coins,idx+1,dic)
        if idx not in dic:
            dic[idx] = {}
        dic[idx][amount] = ans
        return ans

    def change(self, amount: int, coins ) -> int:
        ans = self.recChange(amount,coins,0,{})
        return ans


