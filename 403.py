# -*- coding: utf-8 -*-
# @Time    : 2021-05-25 10:33
# @Author  : zxl
# @FileName: 403.py



class Solution:

    def recJump(self,n,pos,stone_dic,k,dic):
        if pos == n:
            return True
        if pos> n or pos not in stone_dic:
            return False
        if pos in dic and k in dic[pos]:
            return dic[pos][k]
        if pos not in dic:
            dic[pos] = {}
        f1 = False
        if k-1>0:
            f1 = self.recJump(n,pos+k-1,stone_dic,k-1,dic)
        if f1:
            dic[pos][k] = True
            return f1
        f2 = self.recJump(n,pos+k,stone_dic,k,dic)
        if f2:
            dic[pos][k] = True
            return f2
        f3 = self.recJump(n,pos+k+1,stone_dic,k+1,dic)
        if f3:
            dic[pos][k] = True
            return f3
        dic[pos][k] = False
        return False


    def canCross(self, stones ) -> bool:

        stone_dic = {}
        for stone in stones:
            stone_dic[stone] = True

        ans = self.recJump(stones[-1],1,stone_dic,1,{})
        return ans


