# -*- coding: utf-8 -*-
# @Time    : 2021-06-13 15:11
# @Author  : zxl
# @FileName: 299.py



class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        dic = {}
        A = 0
        B = 0

        for i in range(len(secret)):
            if secret[i] not in dic:
                dic[secret[i]] = 0
            if secret[i] == guess[i]:
                A+=1
            else:
                dic[secret[i]] += 1


        for i in range(len(secret)):
            if secret[i] != guess[i]:
                if guess[i] in dic and dic[guess[i]]>0:
                    dic[guess[i]]-=1
                    B+=1
        return str(A)+'A'+str(B)+'B'

